import pytest

from ci_example import add, divide


def test_add() -> None:
    assert add(2, 3) == 5


def test_divide() -> None:
    assert divide(10, 4) == 2.5


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="must not be zero"):
        divide(10, 0)

