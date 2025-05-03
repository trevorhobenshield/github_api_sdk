

from typing import List, Union

from ...._models import BaseModel

__all__ = ["CustomPropertyValue"]


class CustomPropertyValue(BaseModel):
    property_name: str
    """The name of the property"""

    value: Union[str, List[str], None] = None
    """The value assigned to the property"""
