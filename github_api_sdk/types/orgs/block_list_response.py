

from typing import List
from typing_extensions import TypeAlias

from .simple_user import SimpleUser

__all__ = ["BlockListResponse"]

BlockListResponse: TypeAlias = List[SimpleUser]
