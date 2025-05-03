

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ColumnMoveParams"]


class ColumnMoveParams(TypedDict, total=False):
    position: Required[str]
    """The position of the column in a project.

    Can be one of: `first`, `last`, or `after:<column_id>` to place after the
    specified column.
    """
