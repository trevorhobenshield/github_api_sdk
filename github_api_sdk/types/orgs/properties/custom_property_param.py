

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomPropertyParam"]


class CustomPropertyParam(TypedDict, total=False):
    property_name: Required[str]
    """The name of the property"""

    value_type: Required[Literal["string", "single_select", "multi_select", "true_false"]]
    """The type of the value for the property"""

    allowed_values: list[str] | None
    """
    An ordered list of the allowed values of the property. The property can have up
    to 200 allowed values.
    """

    default_value: str | list[str] | None
    """Default value of the property"""

    description: str | None
    """Short description of the property"""

    required: bool
    """Whether the property is required."""

    source_type: Literal["organization", "enterprise"]
    """The source type of the property"""

    url: str
    """
    The URL that can be used to fetch, update, or delete info about this property
    via the API.
    """

    values_editable_by: Literal["org_actors", "org_and_repo_actors"] | None
    """Who can edit the values of the property"""
