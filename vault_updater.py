from argparse import ArgumentParser, FileType, _ArgumentGroup
from json import load as jload

from utils.log import log
from utils.vault import Vault

parser = ArgumentParser(description="Manual update of repositories Vault")
required: _ArgumentGroup = parser.add_argument_group("required arguments")
required.add_argument("-n", "--name", help="Vault name", required=True, metavar="NAME")
required.add_argument(
    "-c", "--cfg", help="path to json config file", required=True, metavar="PATH", type=FileType("r")
)


def main():
    with args.cfg as fobj:
        try:
            data = jload(fobj)
        except Exception:
            log.critical(f"Your {args.config.name} has the wrong JSON structure")
            exit(1)
    db = Vault(args.name)
    for url, branch in data.items():
        db.new_or_update(url, branch)
    db.refresh()


if __name__ == "__main__":
    args = parser.parse_args()
    main()
