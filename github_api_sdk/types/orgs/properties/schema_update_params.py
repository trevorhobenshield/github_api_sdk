

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .custom_property_param import CustomPropertyParam

__all__ = ["SchemaUpdateParams"]


class SchemaUpdateParams(TypedDict, total=False):
    properties: Required[Iterable[CustomPropertyParam]]
    """The array of custom properties to create or update."""
