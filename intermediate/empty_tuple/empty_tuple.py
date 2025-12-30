"""
foo should accept a empty tuple argument.
"""
from typing import Any

def foo(x: tuple[()]) -> Any | None:
    pass