"""A tiny calculator module."""


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def divide(dividend: float, divisor: float) -> float:
    """Divide two numbers, rejecting a zero divisor."""
    if divisor == 0:
        raise ValueError("divisor must not be zero")
    return dividend / divisor

