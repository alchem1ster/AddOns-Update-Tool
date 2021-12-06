from argparse import ArgumentParser, FileType, _ArgumentGroup
from json import load as jload
from pathlib import Path
from subprocess import call
from sys import exit
from time import sleep

from utils.log import log
from utils.updater import AddOnsUpdater
from utils.vault import Vault

parser = ArgumentParser(description="World of Warcraft AddOns update tool")
required: _ArgumentGroup = parser.add_argument_group("required arguments")
required.add_argument("-v", "--vault", help="new or existing Vault name", required=True, metavar="NAME")
required.add_argument("-w", "--wow", help="path to Wow.exe", required=True, metavar="PATH")
parser.add_argument(
    "-s",
    "--start",
    help="start Wow.exe after update",
    action="store_true",
)
parser.add_argument("--verbose", help="verbose debug output", action="store_true")
required.add_argument(
    "-c", "--config", help="path to json config file", required=True, metavar="PATH", type=FileType("r")
)


def main(args: parser):
    if args.verbose:
        log.setLevel(10)
    addons_folder_path: Path = Path(Path(args.wow).parent / "Interface" / "AddOns")
    if not (Path(args.wow).exists() and addons_folder_path.exists()):
        log.critical("Need to specify the correct path to Wow.exe")
        exit(1)
    with args.config as fobj:
        try:
            data = jload(fobj)
        except Exception:
            log.critical(f"Your {args.config.name} has the wrong JSON structure")
            exit(1)
    db = Vault(args.vault)
    for url, branch in data.items():
        db.new_or_update(url, branch)
    db.refresh()
    updater: AddOnsUpdater = AddOnsUpdater(addons_folder_path)
    updater.install(db)
    if args.start:
        log.info("Starting the game..")
        try:
            call(args.wow)
        except Exception:
            log.error("Something went wrong while starting Wow.exe")
    log.warning("Bye-bye! Will close in 5 seconds")
    sleep(5)
    exit(0)


if __name__ == "__main__":
    log.setLevel(20)
    args: parser = parser.parse_args()
    main(args)
