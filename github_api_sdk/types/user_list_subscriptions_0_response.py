

from typing import List
from typing_extensions import TypeAlias

from .minimal_repository import MinimalRepository

__all__ = ["UserListSubscriptions0Response"]

UserListSubscriptions0Response: TypeAlias = List[MinimalRepository]
