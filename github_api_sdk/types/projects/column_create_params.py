

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ColumnCreateParams"]


class ColumnCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the project column"""
