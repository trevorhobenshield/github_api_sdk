

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from ...repos.properties.custom_property_value_param import CustomPropertyValueParam

__all__ = ["ValueUpdateParams"]


class ValueUpdateParams(TypedDict, total=False):
    properties: Required[Iterable[CustomPropertyValueParam]]
    """
    List of custom property names and associated values to apply to the
    repositories.
    """

    repository_names: Required[list[str]]
    """The names of repositories that the custom property values will be applied to."""
