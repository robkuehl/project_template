"""Some example functions."""

from numpy import float64


def add(a: float64, b: float64) -> float64:
    """Function to summarize two values.

    Args:
        a (float64)
        b (float64)

    Returns:
        float64
    """
    return a + b


def div(a: float64, b: float64) -> float64:
    """Function to divide two values.

    Args:
        a (float64): nominator
        b (float64): denominator

    Raises:
        ZeroDivisionError: Raised if b equals 0

    Returns:
        float64
    """
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b


def calc(a: float64, b: float64, operation: str) -> float64:
    """Run calculation with two numbers and an operation as input.

    Args:
        a (float64)
        b (float64)
        operation (str): add, div

    Raises:
        ValueError: If operationen not supported

    Returns:
        float64
    """
    if operation == "add":
        return add(a, b)
    elif operation == "div":
        return div(a, b)
    else:
        raise ValueError("Operation not supported!")
