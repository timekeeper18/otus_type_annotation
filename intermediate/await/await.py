"""
`run_async` takes an awaitable integer.
"""


from collections.abc import Awaitable
from typing import Any


def run_async(func: Awaitable[int]) -> Any | None:
    pass