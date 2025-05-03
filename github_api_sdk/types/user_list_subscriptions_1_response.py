

from typing import List
from typing_extensions import TypeAlias

from .minimal_repository import MinimalRepository

__all__ = ["UserListSubscriptions1Response"]

UserListSubscriptions1Response: TypeAlias = List[MinimalRepository]
