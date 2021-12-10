import sys
from argparse import ArgumentParser, FileType, _ArgumentGroup

from yaml import safe_load

from utils.log import log
from utils.vault import Vault

parser = ArgumentParser(description="Manual update of repositories Vault")
required: _ArgumentGroup = parser.add_argument_group("required arguments")
required.add_argument("-n", "--name", help="Vault name", required=True, metavar="NAME")
required.add_argument("-c", "--cfg", help="path to config file", required=True, metavar="PATH", type=FileType("r"))


def main():
    with args.cfg as fobj:
        try:
            data = safe_load(fobj)
        except Exception:
            log.critical(f"Your {args.config.name} has the wrong Config structure")
            sys.exit(1)
    if data:
        db = Vault(args.name)
        for url, branch in data.items():
            db.new_or_update(url.strip(), branch.strip())
        db.refresh()


if __name__ == "__main__":
    args = parser.parse_args()
    main()
