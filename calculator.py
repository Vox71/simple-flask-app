"""Core arithmetic operations for the calculator."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of two integers."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


_OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def calculate(operation: str, a: int, b: int) -> int | float:
    """Return the result of the requested operation."""
    if operation not in _OPERATIONS:
        raise ValueError(f"unsupported operation: {operation}")
    return _OPERATIONS[operation](a, b)
