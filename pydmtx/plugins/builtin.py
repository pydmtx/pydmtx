import argparse

from pydmtx.plugins import ExportPlugin


class BuiltinExportPlugin(ExportPlugin):
    package_name = "(builtin)"


parser = argparse.ArgumentParser(add_help=False)

parser.add_argument(
    "-b",
    "--background",
    default="0",
    type=str,
    help="description",
)

parser.add_argument(
    "-f",
    "--foreground",
    default="1",
    type=str,
    help="description",
)

parser.add_argument(
    "-n",
    "--newline",
    default="\n",
    type=str,
    help="description",
)

parser.add_argument(
    "-s",
    "--separator",
    default="",
    type=str,
    help="description",
)

parser.add_argument(
    "-a",
    "--append-newline",
    action="store_true",
    help="description",
)

default_options = {
    "background": "0",
    "foreground": "1",
    "newline": "\n",
    "separator": "",
    "append_newline": False,
}


class ExportTextPlugin(BuiltinExportPlugin):
    name = "ExportTextPlugin"
    format_type = "text"
    parser = parser

    def __init__(self, data):
        self.data = data

    def format(self, **options):
        options = {**default_options, **options}

        result = options["newline"].join(map(
            lambda line: options["separator"].join(
                map(
                    lambda module: options["foreground"] if module else options["background"],
                    line
                )
            ),
            self.data
        ))

        if options["append_newline"]:
            result = result + options["newline"]

        return bytes(result, encoding="UTF-8")

    def help(self):
        return "todo"
