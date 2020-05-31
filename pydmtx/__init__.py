from pydmtx.symbol import Symbol
from pydmtx.encode import encode as encode_encode
from pydmtx.reedsolomon import encode as reedsolomon_encode
from pydmtx.bitstream import bitstream
from pydmtx.plugins.registry import plugin_manager

from pydmtx.plugins import ExportPlugin

DEFAULT_QUIET_ZONE = 2
DEFAULT_SYMBOL_SIZE = "square"


class RawSymbol(list):
    def __init__(self, data):
        super().__init__(data)

    def format(self, formatter, **options):
        if isinstance(formatter, str):
            formatter = plugin_manager.find_export_plugin_by_format_type(formatter)

        assert issubclass(formatter, ExportPlugin)

        return formatter(self).format(**options)


def encode(data, quiet_zone=DEFAULT_QUIET_ZONE, version=DEFAULT_SYMBOL_SIZE):
    data = list(bytes(data, encoding="UTF-8"))
    version, data_codewords = encode_encode(data, version)

    data_codewords = bytes(data_codewords)

    codewords = bytes(reedsolomon_encode(data_codewords, version))

    symbol = Symbol(version, quiet_zone=quiet_zone)
    symbol.draw_data(bitstream(codewords))

    raw_symbol = RawSymbol(symbol.raw())

    return raw_symbol
