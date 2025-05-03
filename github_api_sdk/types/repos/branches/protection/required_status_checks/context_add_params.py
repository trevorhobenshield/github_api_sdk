

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ContextAddParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    contexts: Required[list[str]]
    """The name of the status checks"""


class Variant1(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: list[str]
    """The name of the status checks"""


ContextAddParams: TypeAlias = Union[Variant0, Variant1]
