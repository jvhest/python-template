"""Tests goes here."""

from tesje_cc.calculator import add


def test_add() -> None:
    """Test add function."""
    assert add(1, 2) == 3
