from argparse import ArgumentParser
from pathlib import Path

from py_hexdump import hexdump


def main():
    parser = ArgumentParser(prog="py-hexdump")
    parser.add_argument("file")
    parser.add_argument(
        "--width",
        "-w",
        default=2,
        help="how many columns of 8 bytes to display per row. Default=2",
    )
    parser.add_argument(
        "--encoding",
        "-e",
        default=None,
        help="file encoding. Defaults to systems preferred encoding.",
    )

    args = parser.parse_args()

    with Path(args.file).open("rb") as f:
        hexdump(f.read(), width=int(args.width), encoding=args.encoding)


if __name__ == "__main__":
    main()
