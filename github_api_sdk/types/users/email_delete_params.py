

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["EmailDeleteParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    emails: Required[list[str]]
    """Email addresses associated with the GitHub user account."""


class Variant1(TypedDict, total=False):
    body: list[str]


class Variant2(TypedDict, total=False):
    body: str


EmailDeleteParams: TypeAlias = Union[Variant0, Variant1, Variant2]
