"""

`foo` takes keyword arguments of type integer or string.
"""
from typing import Any

def foo(**kwargs: int | str) -> Any | None:
    ...
