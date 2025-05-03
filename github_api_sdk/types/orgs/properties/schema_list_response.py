

from typing import List
from typing_extensions import TypeAlias

from .custom_property import CustomProperty

__all__ = ["SchemaListResponse"]

SchemaListResponse: TypeAlias = List[CustomProperty]
