"""
`foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`.
"""


from typing import Unpack, TypedDict


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]) -> None:
    print(kwargs)

person: Person = {"name": "The Meaning of Life", "age": 1983}
foo(**person)