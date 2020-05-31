from pydmtx.bitstream import bitstream


def test_empty_sequence():
    actual = list(bitstream([]))
    expected = []

    assert actual == expected


def test_sequence_with_one_element():
    actual = list(bitstream([0xfa]))
    expected = [1, 1, 1, 1, 1, 0, 1, 0]

    assert actual == expected


def test_sequence_with_n_elements():
    actual = list(bitstream([1, 2]))
    expected = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]

    assert actual == expected
