import sys
from io import BytesIO
from pathlib import Path
from pickle import dump, load
from re import search as re_search
from shutil import rmtree
from threading import Thread
from typing import List

from dulwich.porcelain import clean, clone, ls_remote, pull, reset
from dulwich.repo import Repo

from utils.log import log
from utils.threads import threaded

custom_outstream: BytesIO = BytesIO()
custom_errstream: BytesIO = BytesIO()


class Repository:
    """The base class of Repository in Vault"""

    head = None

    def __init__(self, url: str, branch: str, basedir: Path):
        self.url: str = url
        try:
            self.author: str = re_search("github.com/(.*)/", url).group(1)
            self.name: str = re_search("(?s:.*)/(.*)", url).group(1)
        except Exception:
            log.error(f"{self.url} seems to be incorrect to process")
            sys.exit(1)
        self.branch: str = branch
        self.basedir: Path = basedir
        self.repo_path: Path = Path(f"{self.basedir}/{self.author}/{self.name}")

    def _reset(self) -> bool:
        """PRIVATE FUNCTION

        Hard reset of Repository

        Returns:
            True: success
            False: fail
        """

        try:
            reset(self.repo_path, "hard")
            clean(self.repo_path, self.repo_path)
        except Exception:
            log.error(f"Something went wrong while cleaning {self.url}@{self.branch}")
            return False
        return True

    def _update(self) -> bool:
        """PRIVATE FUNCTION

        Repository pull from remote

        Returns:
            True: success
            False: fail
        """

        if self._reset():
            try:
                pull(self.repo_path, refspecs=f"refs/heads/{self.branch}".encode())
            except Exception:
                log.error(f"Something went wrong while updating {self.url}@{self.branch}")
                return False
        self.head: str = Repo(self.repo_path).head().decode()
        log.debug(f"Updated: {self.author}/{self.name}@{self.branch}")
        return True

    def check_remote_refs(self) -> bool:
        """Check branch existence on GitHub

        Returns:
            True: branch found
            False: branch not found
        """
        try:
            refs: dict = ls_remote(self.url)
        except Exception:
            log.error(f"Something went wrong while checking {self.author}/{self.name} remote refs")
            return False
        branch_ref: str = f"refs/heads/{self.branch}".encode()
        if branch_ref not in refs.keys():
            log.error(f"{self.name}@{self.branch} doesnt exist on GitHub")
            return False
        return True

    def download(self) -> "bool | int":
        """Download Repository if not exist or update if exist

        Returns:
            True: downloaded
            -1:  already exist and has been successfully updated
            False: fail
        """

        try:
            self.repo_path.mkdir(parents=True, exist_ok=True)
            clone(
                self.url,
                self.repo_path,
                checkout=True,
                branch=self.branch.encode(),
                errstream=custom_errstream,
                outstream=custom_outstream,
            )
        except Exception as e:
            if type(e) == FileExistsError:
                if self._update():
                    return -1
            log.error(f"Something went wrong while saving {self.url}@{self.branch} into {self.repo_path}")
            return False
        self.head: str = Repo(self.repo_path).head().decode()
        log.debug(f"Downloaded: {self.author}/{self.name}@{self.branch}")
        return True

    def remove(self) -> bool:
        """Remove Repository from Vault

        Returns:
            True: success
            False: fail
        """

        try:
            rmtree(self.repo_path)
        except Exception:
            log.warning(f"Something went wrong while removing {self.author}/{self.name} from Vault")
            return False
        return True

    def checkout(self, old_branch: str) -> bool:
        """Change branch of Repository

        Args:
            old_branch (str): name of cached branch

        Returns:
            True: branch changed
            False: checkout fail
        """

        log.warning(f"{self.author}/{self.name} will have its branch changed from @{old_branch} to @{self.branch}")
        try:
            rmtree(self.repo_path)
            self.download()
        except Exception:
            log.error(f"Something went wrong while checkout {self.author}/{self.name}")
            return False
        return True


class Vault:
    """The base class of repositories Vault"""

    repositories: List[Repository] = []
    cache_db_path: Path = Path("./cache.db")
    threads: List[Thread] = []
    session: List[Repository] = []

    def __init__(self, name: str) -> None:
        self.basedir: Path = Path("./vault" / Path(name))
        if not (self.basedir.is_dir() or self.basedir.exists()):
            log.warning(f'Path "{Path.cwd() / self.basedir}" not found. Let\'s create..')
            self.basedir.mkdir(parents=True, exist_ok=True)
        self.cache_db_path: Path = self.basedir / self.cache_db_path
        if not self.cache_db_path.exists():
            try:
                with open(self.cache_db_path, "wb") as cache_db:
                    dump(self.repositories, cache_db)
            except Exception:
                log.critical("Something went wrong while saving Vault DB")
                sys.exit(1)
        self._load()
        log.info(f"Vault loaded: {self.basedir.name}")
        log.info(f"Repositories in Vault cache: {len(self.repositories)}")

    def _load(self) -> None:
        """PRIVATE FUNCTION

        Load of Vault database"""

        try:
            with open(self.cache_db_path, "rb") as cache_db:
                cached_db: List[Repository] = load(cache_db)
        except Exception:
            log.critical("Something went wrong while loading Vault DB")
            sys.exit(1)
        self.repositories.clear()
        for repository in cached_db:
            if repository.repo_path not in [x.repo_path for x in self.repositories]:
                self.repositories.append(repository)

    @threaded
    def new_or_update(self, url: str, branch: str) -> None:
        """Create new Repository in Vault (or update exist in child function)

        Args:
            url (str): link to github repository
            branch (str): branch of github repository to download/update
        """

        repository: Repository = Repository(url, branch, self.basedir)
        if not repository.check_remote_refs():
            if in_cache := [x for x in self.repositories if x.repo_path == repository.repo_path]:
                self.session.append(in_cache[0])
            return
        for cached_repository in self.repositories:
            if (
                cached_repository.repo_path == repository.repo_path
                and (old_branch := cached_repository.branch) != repository.branch
            ):
                repository.checkout(old_branch)
                break
        else:
            repository.download()
        self.session.append(repository)

    def refresh(self) -> None:
        """Refresh Vault database"""

        for thread in self.threads:
            thread.join()
        self.repositories: List[Repository] = self.session
        try:
            with open(self.cache_db_path, "wb") as cache_db:
                dump(self.repositories, cache_db)
        except Exception:
            log.critical("Something went wrong while saving Vault DB")
            sys.exit(1)
        self._load()
        log.info(f"Vault updated: {self.basedir.name}")
        log.info(f"Repositories in Vault: {len(self.repositories)}")
