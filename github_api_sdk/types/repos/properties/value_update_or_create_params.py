

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .custom_property_value_param import CustomPropertyValueParam

__all__ = ["ValueUpdateOrCreateParams"]


class ValueUpdateOrCreateParams(TypedDict, total=False):
    owner: Required[str]

    properties: Required[Iterable[CustomPropertyValueParam]]
    """
    A list of custom property names and associated values to apply to the
    repositories.
    """
