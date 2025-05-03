

from typing import List
from typing_extensions import TypeAlias

from .orgs.simple_user import SimpleUser

__all__ = ["UserListFollowers0Response"]

UserListFollowers0Response: TypeAlias = List[SimpleUser]
