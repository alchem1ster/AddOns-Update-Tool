import sys
from argparse import ArgumentParser, _ArgumentGroup
from json import load as jload
from pathlib import Path
from subprocess import call
from time import sleep

from utils.log import log
from utils.updater import AddOnsUpdater
from utils.vault import Vault

parser = ArgumentParser(description="World of Warcraft AddOns update tool")
required: _ArgumentGroup = parser.add_argument_group("required arguments")
required.add_argument("-v", "--vault", help="new or existing Vault name", metavar="NAME", nargs="?", const="")
required.add_argument("-w", "--wow", help="path to Wow.exe", metavar="PATH", nargs="?", const="")
parser.add_argument(
    "-s",
    "--start",
    help="start Wow.exe after update",
    action="store_true",
)
parser.add_argument("--verbose", help="verbose debug output", action="store_true")
required.add_argument("-c", "--config", help="path to json config file", metavar="PATH", nargs="?", const="")


def process_args(args):
    if len(sys.argv) == 1:
        args.verbose = True
        log.setLevel(10)
    if not args.vault:
        log.debug("Vault name is not specified, will be used default name: github")
        args.vault = "github"
    if not args.wow:
        log.debug("Path to Wow.exe is not specified, will be used from the current directory")
        args.wow = Path(".\Wow.exe")
    if not args.config:
        log.debug("Path to config.json is not specified, will be used from the current directory")
        args.config = Path(".\config.json")


def main(args):
    if args.verbose:
        log.setLevel(10)
    process_args(args)
    addons_folder_path: Path = Path(Path(args.wow).parent / "Interface" / "AddOns")
    if not (Path(args.wow).exists() and addons_folder_path.exists()):
        log.critical("Need to specify the correct path to Wow.exe")
        sys.exit(1)
    if Path(args.config).exists():
        with open(args.config, "r") as fobj:
            try:
                data = jload(fobj)
            except Exception:
                log.critical(f"Your {args.config.name} has the wrong JSON structure")
                sys.exit(1)
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
    sys.exit(0)


if __name__ == "__main__":
    log.setLevel(20)
    args = parser.parse_args()
    main(args)
