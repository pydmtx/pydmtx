import argparse
import sys
from pathlib import Path
# from pydmtx.core import
from pydmtx.cli.argparser import ArgParser, SIZE_CHOICES
from pydmtx import plugin_manager, encode

def check_nonnegative_int(value):
    try:
        integer = int(value)
    except:
        raise argparse.ArgumentTypeError(f"'{value}' is an invalid int value")

    if integer < 0:
        raise argparse.ArgumentTypeError(f"'{value}' is an invalid nonnegative int value")

    return integer


def source(value):
    # TODO
    return value
    # https://github.com/python/cpython/blob/master/Lib/argparse.py#L1227
    if value == "-" or Path(value).is_file():
        return argparse.FileType("rb")(value).read()

    return value


parser = ArgParser(
    prog="pydmtx",
    usage="%(prog)s [SOURCE] [OPTIONS] [--] [EXPORT_OPTIONS]",
    description="program description",
    epilog="epilog",
    allow_abbrev=False,
)

parser.add_argument(
    "data_to_encode",
    metavar="SOURCE",
    type=source,
    help="when SOURCE is -, then read from stdin",
)

parser.add_argument(
    "-q",
    "--quiet-zone",
    metavar="INT",
    action="store",
    type=check_nonnegative_int,
    default=2,
    help="description [default: %(default)s]",
)

parser.add_argument(
    "-s",
    "--size",
    metavar="SIZE",
    action="store",
    type=str,
    choices=SIZE_CHOICES,
    default="square",
    help="description [default: %(default)s] [choices: %(choices)s]"
)

available_export_formats = [plugin.format_type for plugin in plugin_manager.find_export_plugins()]

parser.add_argument(
    "-f",
    "--format",
    metavar="FORMAT",
    action="store",
    choices=available_export_formats,
    default="text",
    help="description [default: %(default)s] [choices: %(choices)s]",
)

parser.add_argument(
    "-o",
    "--output",
    action="store",
    type=str,
    help="description",
)

parser.add_argument(
    "--stdout",
    action="store_true",
    help="description",
)

parser.add_argument(
    "-p",
    "--preview",
    action="store_true",
    help="description",
)

parser.add_argument(
    "--format-help",
    metavar="FORMAT",
    action="store",
    type=str,
    choices=available_export_formats,
    help=f"description [choices: %(choices)s]",
)

parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="%(prog)s 0.1.0",
)

def main():
    args, export_args = parser.parse_args()

    data_to_encode = source(args.data_to_encode)

    formatter = plugin_manager.find_export_plugin_by_format_type(args.format)
    raw_symbol = encode(data_to_encode, version=args.size, quiet_zone=args.quiet_zone)

    formatter_options = vars(formatter.parser.parse_args(export_args))
    result = raw_symbol.format(formatter, **formatter_options)

    if args.output:
        with open(args.output, "wb") as f:
            f.write(result)
    elif args.stdout:
        sys.stdout.buffer.write(result)

    return 0
