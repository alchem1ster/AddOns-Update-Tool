import sys
from datetime import datetime
from glob import glob
from pathlib import Path
from pickle import dump, load
from shutil import copytree, move, rmtree
from threading import Lock, Thread
from typing import Dict, List, Tuple

from utils.log import log
from utils.threads import threaded
from utils.vault import Vault

lock: Lock = Lock()


class AddOnsUpdater:
    """The base class of AddOns updating service"""

    cache: Dict[str, str] = {}
    threads: List[Thread] = []

    def __init__(self, path_to_addons_folder: Path):
        self.addons_folder: Path = path_to_addons_folder
        self.interface_folder: Path = path_to_addons_folder.parent
        self.addons_backup_folder: Path = self.interface_folder / "AddOns_backups"
        self.addons_backup_folder.mkdir(parents=True, exist_ok=True)
        self.updater_cache_db_path: Path = self.interface_folder / "updater_cache.db"
        if not self.updater_cache_db_path.exists():
            try:
                with open(self.updater_cache_db_path, "wb") as cache_db:
                    dump(self.cache, cache_db)
            except Exception:
                log.critical("Something went wrong while saving AddOnsUpdater DB")
                sys.exit(1)
        else:
            try:
                with open(self.updater_cache_db_path, "rb") as cache_db:
                    self.cache: Dict[str, str] = load(cache_db)
            except Exception:
                log.critical("Something went wrong while loading AddOnsUpdater DB")
                sys.exit(1)
        log.info("Game folder initialized")

    def _backup_init(self) -> None:
        """PRIVATE FUNCTION

        Create a directory for saving backups"""

        timestamp: str = datetime.now().replace(microsecond=0).isoformat().replace(":", "-")
        self.timestamp_backup_folder: Path = Path(self.addons_backup_folder / timestamp)
        self.timestamp_backup_folder.mkdir(parents=True, exist_ok=True)

    def _backup_end(self) -> None:
        """PRIVATE FUNCTION

        Remove empty and old backup folders"""

        if next(self.timestamp_backup_folder.iterdir(), None) is None:
            self.timestamp_backup_folder.rmdir()
            log.info("There is nothing to backup, skipped")
        else:
            log.info("All updatable AddOns has beed saved")
            all_backups: Path = [
                folder for folder in sorted(self.addons_backup_folder.iterdir(), key=lambda i: i.name, reverse=True)
            ]
            if len(all_backups) > 5:
                log.debug("Removing old backup folders, keeping only last 5 backups")
                for folder in all_backups[5:]:
                    try:
                        rmtree(folder)
                    except Exception:
                        log.error("Something went wrong while deleting old backups")

    @threaded
    def _backup(self, addon_to_backup: str) -> None:
        """PRIVATE FUNCTION

        Backup AddOn folder from game

        Args:
            addon_to_backup (str): AddOn name (folder name) to backup
        """

        addon_dir: Path = Path(self.addons_folder / addon_to_backup)
        if addon_dir.exists():
            try:
                move(str(addon_dir), str(self.timestamp_backup_folder))
            except Exception:
                log.error(f"Something went wrong while saving {addon_dir.name} backup")
                return
            log.debug(f"{addon_dir.name} backup has been saved")

    @threaded
    def _copy(self, addon_to_install: List[List]) -> None:
        """PRIVATE FUNCTION

        Copy AddOn from Vault DB to game folder and update AddOnsUpdater DB

        Args:
            addon_to_install (List[List]): list of AddOn folders
        """

        repo_name: str = addon_to_install[0]
        repo_head: str = addon_to_install[1]
        dirs_tocopy_list: List[Path] = addon_to_install[2]
        for folder in dirs_tocopy_list:
            try:
                copytree(str(folder), str(self.addons_folder / folder.name))
            except Exception:
                log.error(f"Something went wrong while updating {repo_name}")
                return
            with lock:
                self.cache[repo_name] = repo_head
            if repo_head and repo_name:
                log.debug(f"{repo_name}@{repo_head[:7]} has been installed")

    def install(self, vault: Vault) -> None:
        """Backup and Install/Update AddOns

        Args:
            vault (Vault): Vault instance
        """

        addons_to_backup, addons_to_install = self._prepare(vault)
        if addons_to_backup:
            self._backup_init()
            for addon_to_backup in addons_to_backup:
                self._backup(addon_to_backup)
            for thread in self.threads:
                thread.join()
            self._backup_end()
        if addons_to_install:
            for addon in addons_to_install:
                self._copy(addon)
            for thread in self.threads:
                thread.join()
            try:
                with open(self.updater_cache_db_path, "wb") as cache_db:
                    dump(self.cache, cache_db)
            except Exception:
                log.critical("Something went wrong while saving AddOnsUpdater DB")
                sys.exit(1)
        log.info("All AddOns up to date")

    def _prepare(self, vault: Vault) -> Tuple[List[str], List[List]]:
        """PRIVATE FUNCTION

        Parse and prepare Vault repositories

        Args:
            vault (Vault): Vault instance

        Returns:
            Tuple[List[str], List[List]]: lists of addons to backup and install
        """

        addons_to_backup: List[str] = []
        addons_to_install: List[List] = []
        for repository in vault.repositories:
            if repository.name not in self.cache.keys():
                log.info(f"{repository.name} will be installed")
            elif repository.head != self.cache[repository.name]:
                log.info(f"{repository.name} will be updated")
            else:
                continue
            to_copy: List[Path] = [Path(x).parent for x in glob(str(repository.repo_path / "*.toc"))] or [
                Path(x).parent for x in glob(str(repository.repo_path / "*" / "*.toc"))
            ]
            to_backup: List[str] = [Path(x).parent.name for x in glob(str(repository.repo_path / "*.toc"))] or [
                Path(x).parent.name for x in glob(str(repository.repo_path / "*" / "*.toc"))
            ]
            addons_to_backup.extend(to_backup)
            addons_to_install.append([repository.name, repository.head, to_copy])
        return addons_to_backup, addons_to_install
