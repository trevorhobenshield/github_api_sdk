

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["CustomPropertyValueParam"]


class CustomPropertyValueParam(TypedDict, total=False):
    property_name: Required[str]
    """The name of the property"""

    value: Required[str | list[str] | None]
    """The value assigned to the property"""
