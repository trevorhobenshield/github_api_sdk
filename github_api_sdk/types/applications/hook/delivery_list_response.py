

from typing import List
from typing_extensions import TypeAlias

from .item import Item

__all__ = ["DeliveryListResponse"]

DeliveryListResponse: TypeAlias = List[Item]
