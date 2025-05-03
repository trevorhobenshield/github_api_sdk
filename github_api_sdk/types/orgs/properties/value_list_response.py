

from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel
from ...repos.properties.custom_property_value import CustomPropertyValue

__all__ = ["ValueListResponse", "ValueListResponseItem"]


class ValueListResponseItem(BaseModel):
    properties: List[CustomPropertyValue]
    """List of custom property names and associated values"""

    repository_full_name: str

    repository_id: int

    repository_name: str


ValueListResponse: TypeAlias = List[ValueListResponseItem]
