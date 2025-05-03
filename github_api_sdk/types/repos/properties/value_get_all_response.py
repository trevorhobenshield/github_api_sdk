

from typing import List
from typing_extensions import TypeAlias

from .custom_property_value import CustomPropertyValue

__all__ = ["ValueGetAllResponse"]

ValueGetAllResponse: TypeAlias = List[CustomPropertyValue]
