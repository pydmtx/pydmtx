from pydmtx.encode import encode


def test_encode_ascii_1234569():
    data_to_encode = list(b"1234569")

    _, actual = encode(data_to_encode)
    expected = [142, 164, 186, 58, 129]

    assert actual == expected


def test_encode_ascii_Aa999():
    data_to_encode = list(b"Aa999")

    _, actual = encode(data_to_encode)
    expected = [66, 98, 229, 58, 129]

    assert actual == expected


def test_encode_ascii_AAAAAAAAA():
    data_to_encode = list(b"AAAAAAAAA")

    _, actual = encode(data_to_encode)
    expected = [66, 66, 66, 66, 66, 66, 66, 66, 66, 129, 101, 251]

    assert actual == expected
