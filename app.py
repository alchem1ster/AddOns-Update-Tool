"""Main module CLI"""

import sys
from argparse import ArgumentParser, _ArgumentGroup
from pathlib import Path
from subprocess import call
from time import sleep

from yaml import safe_load

from utils.log import log
from utils.updater import AddOnsUpdater
from utils.vault import Vault

parser = ArgumentParser(description="World of Warcraft AddOns update tool")
required: _ArgumentGroup = parser.add_argument_group("required arguments")
required.add_argument(
    "-v",
    "--vault",
    help="new or existing Vault name",
    metavar="NAME",
    nargs="?",
    const="",
)
required.add_argument(
    "-w", "--wow", help="path to Wow.exe", metavar="PATH", nargs="?", const=""
)
parser.add_argument(
    "-s",
    "--start",
    help="start Wow.exe after update",
    action="store_true",
)
parser.add_argument(
    "--verbose", help="verbose debug output", action="store_true"
)
required.add_argument(
    "-c",
    "--config",
    help="path to config file",
    metavar="PATH",
    nargs="?",
    const="",
)


def process_args():
    """Process passed arguments"""

    if len(sys.argv) == 1:
        args.verbose = True
        log.setLevel(10)
    if not args.vault:
        log.debug(
            "Vault name is not specified, will be used default name: github"
        )
        args.vault = "github"
    if not args.wow:
        log.debug(
            "Path to Wow.exe is not specified, will be used from the current"
            " directory"
        )
        args.wow = Path(".\\Wow.exe")
    if not args.config:
        log.debug(
            "Path to config file is not specified, will be used from the"
            " current directory"
        )
        if (
            (config_file := Path(".\\config.yaml")) and config_file.exists()
        ) or (
            (config_file := Path(".\\config.json")) and config_file.exists()
        ):
            args.config = config_file
        else:
            log.critical(
                "Neither 'config.yaml' nor 'config.json' file was found in"
                " current directory"
            )
            sys.exit(1)


def main():
    """Entry point"""

    if args.verbose:
        log.setLevel(10)
    process_args()
    addons_folder_path: Path = Path(
        Path(args.wow).parent / "Interface" / "AddOns"
    )
    if not (Path(args.wow).exists() and addons_folder_path.exists()):
        log.critical("Need to specify the correct path to Wow.exe")
        sys.exit(1)
    if Path(args.config).exists():
        with open(args.config, "r", encoding="utf-8") as fobj:
            try:
                data = safe_load(fobj)
            except Exception:
                log.critical(
                    "Your %s has the wrong Config structure", args.config
                )
                sys.exit(1)
    else:
        log.critical("%s not found", args.config)
        sys.exit(1)
    if data:
        vault_db = Vault(args.vault)
        for url, branch in data.items():
            vault_db.new_or_update(url.strip(), branch.strip())
        vault_db.refresh()
        updater: AddOnsUpdater = AddOnsUpdater(addons_folder_path, vault_db)
        updater.install()
        if args.start:
            log.info("Starting the game..")
            try:
                call(args.wow)
            except Exception:
                log.error("Something went wrong while starting Wow.exe")
    log.warning("Bye-bye! Will close in 5 seconds")
    sleep(5)
    sys.exit(0)


if __name__ == "__main__":
    log.setLevel(20)
    args = parser.parse_args()
    main()
