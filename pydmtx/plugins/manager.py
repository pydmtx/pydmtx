from pkg_resources import iter_entry_points

from pydmtx.plugins.base import BasePlugin, ExportPlugin
from pydmtx.plugins.exceptions import NotFoundExportPlugin

ENTRY_POINT_NAMES = [
    "pydmtx.plugins.export",
]


class PluginManager(list):
    def register(self, *plugins):
        self.extend(plugins)

    def unregister(self, plugin):
        self.remove(plugin)

    def filter(self, by_type):
        for plugin in self:
            if issubclass(plugin, by_type):
                yield plugin

    def load_installed_plugins(self):
        for entry_point_name in ENTRY_POINT_NAMES:
            for entry_point in iter_entry_points(entry_point_name):
                plugin = entry_point.load()
                plugin.package_name = entry_point.dist.key
                self.register(plugin)

    def find_export_plugins(self):
        return self.filter(ExportPlugin)

    def find_export_plugin_by_format_type(self, format_type):
        for plugin in self.find_export_plugins():
            if plugin.format_type == format_type:
                return plugin

        raise NotFoundExportPlugin(format_type)

    def __repr__(self):
        return f"<PluginManager: {list(self)}"
