

from typing import List
from typing_extensions import TypeAlias

from .orgs.simple_user import SimpleUser

__all__ = ["UserListFollowers1Response"]

UserListFollowers1Response: TypeAlias = List[SimpleUser]
