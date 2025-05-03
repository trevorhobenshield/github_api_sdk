

from typing import List
from typing_extensions import TypeAlias

from .simple_user import SimpleUser

__all__ = ["TeamListMembersResponse"]

TeamListMembersResponse: TypeAlias = List[SimpleUser]
