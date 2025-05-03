

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardMoveParams"]


class CardMoveParams(TypedDict, total=False):
    position: Required[str]
    """The position of the card in a column.

    Can be one of: `top`, `bottom`, or `after:<card_id>` to place after the
    specified card.
    """

    column_id: int
    """The unique identifier of the column the card should be moved to"""
