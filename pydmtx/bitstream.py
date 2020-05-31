from itertools import chain

def bitstream(ubytes):
    for ubyte in ubytes:
        assert 0 <= ubyte <= 255

        for offset in reversed(range(8)):
            yield (ubyte >> offset) & 1
