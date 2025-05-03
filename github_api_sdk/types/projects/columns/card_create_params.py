

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["CardCreateParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    note: Required[str | None]
    """The project card's note"""


class Variant1(TypedDict, total=False):
    content_id: Required[int]
    """The unique identifier of the content associated with the card"""

    content_type: Required[str]
    """The piece of content associated with the card"""


CardCreateParams: TypeAlias = Union[Variant0, Variant1]
