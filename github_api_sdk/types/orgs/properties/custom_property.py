

from typing import List, Union, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CustomProperty"]


class CustomProperty(BaseModel):
    property_name: str
    """The name of the property"""

    value_type: Literal["string", "single_select", "multi_select", "true_false"]
    """The type of the value for the property"""

    allowed_values: Optional[List[str]] = None
    """
    An ordered list of the allowed values of the property. The property can have up
    to 200 allowed values.
    """

    default_value: Union[str, List[str], None] = None
    """Default value of the property"""

    description: Optional[str] = None
    """Short description of the property"""

    required: Optional[bool] = None
    """Whether the property is required."""

    source_type: Optional[Literal["organization", "enterprise"]] = None
    """The source type of the property"""

    url: Optional[str] = None
    """
    The URL that can be used to fetch, update, or delete info about this property
    via the API.
    """

    values_editable_by: Optional[Literal["org_actors", "org_and_repo_actors"]] = None
    """Who can edit the values of the property"""
