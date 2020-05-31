from pydmtx.plugins.manager import PluginManager
from pydmtx.plugins.builtin import ExportTextPlugin

plugin_manager = PluginManager()

plugin_manager.load_installed_plugins()

plugin_manager.register(ExportTextPlugin)
