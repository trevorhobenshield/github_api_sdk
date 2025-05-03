

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["TeamRemoveParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    teams: Required[list[str]]
    """The slug values for teams"""


class Variant1(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: list[str]
    """The slug values for teams"""


TeamRemoveParams: TypeAlias = Union[Variant0, Variant1]
