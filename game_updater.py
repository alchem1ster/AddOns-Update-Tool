"""Ingame AddOns update CLI"""

import sys
from argparse import ArgumentParser, _ArgumentGroup
from glob import glob
from pathlib import Path

from utils.log import log
from utils.updater import AddOnsUpdater
from utils.vault import Vault

parser = ArgumentParser(
    description="Manual update of addons in game directory"
)
required: _ArgumentGroup = parser.add_argument_group("required arguments")
required.add_argument(
    "-n", "--name", help="existing Vault name", required=True, metavar="NAME"
)
required.add_argument(
    "-w", "--wow", help="path to WoW.exe", required=True, metavar="PATH"
)


def main():
    """Entry point"""

    if Path(f"./vault/{args.name}").exists():
        vault_db: Vault = Vault(args.name)
    else:
        log.critical("Vault name ./vault/%s doest not exist", args.name)
        log.critical(
            "Available Vaults: %s",
            ", ".join(Path(x).name for x in glob("./vault/*")),
        )
        sys.exit(1)
    addons_folder_path: Path = Path(
        Path(args.wow).parent / "Interface" / "AddOns"
    )
    if not (Path(args.wow).exists() and addons_folder_path.exists()):
        log.critical("Need to specify the correct path to Wow.exe")
        sys.exit(1)

    updater: AddOnsUpdater = AddOnsUpdater(addons_folder_path, vault_db)
    updater.install()


if __name__ == "__main__":
    args: parser = parser.parse_args()
    main()
