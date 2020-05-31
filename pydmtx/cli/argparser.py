import argparse

from pydmtx import plugin_manager

SIZE_CHOICES = ["square", "rectangle", "10", "12", "14", "16", "18", "20", "22", "24", "26", "32", "36", "40", "44", "48", "52", "64", "72", "80", "88", "96", "104", "120", "132", "144", "8x18", "8x32", "12x26", "12x36", "16x36", "16x48"]


class HelpFormatter(argparse.RawDescriptionHelpFormatter):
    def __init__(self, *args, **kwargs):
        kwargs["width"] = 70
        super().__init__(*args, **kwargs)


class ArgParser(argparse.ArgumentParser):
    """Adds additional logic to `argparse.ArgumentParser`."""

    def __init__(self, *args, formatter_class=HelpFormatter, **kwargs):
        super().__init__(*args, formatter_class=formatter_class, **kwargs)
        self.args = None
        self.export_args = None

    def parse_args(self, args=None):
        self.args, export_args = super().parse_known_args(args)

        self._exit_if_format_help_option()
        self._set_version()
        self._find_export_args(export_args)

        return self.args, self.export_args

    def _exit_if_format_help_option(self):
        if self.args.format_help:
            format_type = self.args.format_help

            try:
                plugin = plugin_manager.find_export_plugin_by_format_type(format_type)

                print(plugin.parser.print_help())
            except:
                pass

            self.exit()

    def _set_version(self):
        if self.args.size not in ("square", "rectangle"):
            self.args.size = SIZE_CHOICES.index(self.args.size) - 2

    def _find_export_args(self, export_args):
        if "--" in export_args:
            double_dash_position = export_args.index("--")
            self.export_args = export_args[double_dash_position + 1:]
        else:
            self.export_args = []
