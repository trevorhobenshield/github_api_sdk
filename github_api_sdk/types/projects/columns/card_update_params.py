

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CardUpdateParams"]


class CardUpdateParams(TypedDict, total=False):
    archived: bool
    """Whether or not the card is archived"""

    note: str | None
    """The project card's note"""
