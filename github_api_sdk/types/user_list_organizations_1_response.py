

from typing import List
from typing_extensions import TypeAlias

from .organization import Organization

__all__ = ["UserListOrganizations1Response"]

UserListOrganizations1Response: TypeAlias = List[Organization]
