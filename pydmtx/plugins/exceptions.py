class PluginError(Exception):
    pass

class NotFoundExportPlugin(PluginError):
    def __init__(self, format_type):
        self.format_type = format_type
    
    def __str__(self):
        return f"Plugin (format_type='{self.format_type}') not found."
