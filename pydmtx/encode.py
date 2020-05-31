ASCII_PAD = 129
UPPER_SHIFT = 235

total_data_codewords = [
    3, 5, 8, 12, 18, 22, 30, 36, 44, 62, 86, 114, 144, 174, 204,
    280, 368, 456, 576, 696, 816, 1050, 1304, 1558, 5, 10, 16, 22, 32, 49
]


def encode(data, version="square", encoding="ascii"):
    codewords = _encode_ascii(data)
    codewords_length = len(codewords)

    version = _find_symbol(codewords_length, version)
    pad_length = total_data_codewords[version] - codewords_length

    return version, codewords + _randomize_253_state(codewords_length, pad_length)


def _encode_ascii(data):
    encoded = []
    length = len(data)
    i = 0

    while i < length:
        current = data[i]
        nxt = data[i + 1] if i + 1 < length else None

        if nxt and (48 <= data[i] <= 57) and (48 <= data[i + 1] <= 57):
            encoded.append(130 + (data[i] - 48)  * 10 + data[i + 1] - 48)
            i += 1
        elif 0 <= data[i] <= 127:
            encoded.append(data[i] + 1)
        elif 128 <= data[i] <= 255:
            encoded.append(UPPER_SHIFT)
            encoded.append(data[i] - 128 + 1)

        i += 1
    
    return encoded


def _find_symbol(length, version):
    assert version in ("square", "rectangle") or 0 <= version <= 29

    if isinstance(version, int):
        if length <= total_data_codewords[version]:
            return version
        else:
            raise ValueError("Specified version is too small for the data.")
    elif version == "rectangle":
        return _find_symbol_by_offset(length, 24)

    return _find_symbol_by_offset(length, 0)


def _find_symbol_by_offset(length, offset):
    for index, capacity in enumerate(total_data_codewords[offset:]):
        if length <= capacity:
            return offset + index

    raise ValueError("The data is too long.")


def _randomize_253_state(pad_codeword_position, pad_length):
    pad = [ASCII_PAD]

    position = pad_codeword_position + 1

    for i in range(pad_length - 1):
        pseudo_random = ASCII_PAD + ((149 * position) % 253) + 1

        if pseudo_random > 254:
            pseudo_random -= 254

        pad.append(pseudo_random)
        position += 1

    return [] if pad_length == 0 else pad
