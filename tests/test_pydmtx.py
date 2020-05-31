import sys
import textwrap
import unittest
from pathlib import Path

import pydmtx
import pytest


def test_quiet_zone():
    expected = textwrap.dedent("""\
    █░█░█░█░█░█░█░█░
    █░█░█░█░█░░░░░░█
    █░█░█░█░███░██░░
    █░█░█░█░█░██░░██
    █░█░█░█░█░░░██░░
    █░█░█░█░█░░░██░█
    █░█░█░█░█░░░░█░░
    █░█░█░█░░██░█░░█
    █░█░█░█░█░░░░██░
    █░░░░░█░░█░██░░█
    █████████░░░░█░░
    ██░██░░██░░█░█░█
    ███████░░██░░█░░
    ███░░█░████░░█░█
    ███░░█░░█░█░░░█░
    ████████████████""")

    actual = pydmtx.encode("30Q324343430794<OQQ", quiet_zone=0).format("text", background="░", foreground="█")

    assert str(actual, encoding="utf-8") == expected


def test_ascii_encoding():
    expected = textwrap.dedent("""\
    ░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░
    ░░█░█░█░█░█░░░
    ░░██░░█░██░█░░
    ░░██░░░░░█░░░░
    ░░██░░░███░█░░
    ░░██░░░░█░░░░░
    ░░█░░░░░████░░
    ░░███░██░░░░░░
    ░░████░██░░█░░
    ░░█░░███░█░░░░
    ░░██████████░░
    ░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░""")

    actual = pydmtx.encode("123456").format("text", foreground="█", background="░")

    assert str(actual, encoding="utf-8") == expected


@pytest.mark.skip(reason="unimplemented")
def test_optimized_encoding():
    expected = textwrap.dedent("""\
    █░█░█░█░█░█░█░█░█░
    █░█░░░█░█░█░░░████
    █░██░░░░░███░░░░█░
    █░░░░░█░███░█░░███
    █░░█░░░░░█░░░███░░
    █░█░█████░█░█░████
    █░░██░░███████░██░
    ██░░███░████████░█
    ██████████░█████░░
    █░███░██░█░░█░██░█
    █░░░█░██░█░█░░███░
    █░██░████░░██░░░░█
    ██░░░██░█░█░░████░
    ██░██░█░░░░░█░░░██
    █░██░█░░██░█░██░█░
    █░░░█░░██░░█░██░██
    █░░░██░░░░░░█░░█░░
    ██████████████████""")

    actual = pydmtx.encode("A1B2C3D4E5F6G7H8I9J0K1L2", quiet_zone=0).format("text", background="░", foreground="█")

    assert str(actual, encoding="utf-8") == expected
