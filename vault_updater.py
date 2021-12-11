"""Vault update CLI"""

import sys
from argparse import ArgumentParser, FileType, _ArgumentGroup

from yaml import safe_load

from utils.log import log
from utils.vault import Vault

parser = ArgumentParser(description="Manual update of repositories Vault")
required: _ArgumentGroup = parser.add_argument_group("required arguments")
required.add_argument(
    "-n", "--name", help="Vault name", required=True, metavar="NAME"
)
required.add_argument(
    "-c",
    "--cfg",
    help="path to config file",
    required=True,
    metavar="PATH",
    type=FileType("r"),
)


def main():
    """Entry point"""

    with args.cfg as fobj:
        try:
            data = safe_load(fobj)
        except Exception:
            log.critical(
                "Your %s has the wrong Config structure", args.config.name
            )
            sys.exit(1)
    if data:
        vault_db = Vault(args.name)
        for url, branch in data.items():
            vault_db.new_or_update(url.strip(), branch.strip())
        vault_db.refresh()


if __name__ == "__main__":
    args = parser.parse_args()
    main()
