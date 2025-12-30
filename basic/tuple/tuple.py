"""
foo should accept a tuple argument, 1st item is a string, 2nd item is an integer.
"""
from typing import Any

def foo(x: tuple[str, int]) -> Any | None:
    pass
