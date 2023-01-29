"""Tests goes here."""

from {{ cookiecutter.__package_name }}.calculator import add


def test_add() -> None:
    """Test add function."""
    assert add(1, 2) == 3
