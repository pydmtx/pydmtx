from pydmtx.reedsolomon import encode


def test_encode():
    actual = encode([0x8e, 0xa4, 0xba], 0)
    expected = [0x8e, 0xa4, 0xba, 0x72, 0x19, 0x05, 0x58, 0x66]

    assert actual == expected