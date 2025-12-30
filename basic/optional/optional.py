"""
foo can accept an integer argument, None or no argument at all.
"""
from typing import Any

def foo(x: int | None = 0) -> Any | None:
    pass
