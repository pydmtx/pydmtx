class BasePlugin:
    name = None
    description = None
    package_name = None


class ExportPlugin(BasePlugin):
    format_type = None

    def format(self):
        raise NotImplementedError()

    def help(self):
        return f"For help check the official documentation for '{self.package_name}' plugin."
