

from typing import List
from typing_extensions import TypeAlias

from .repository_invitation import RepositoryInvitation

__all__ = ["InvitationListResponse"]

InvitationListResponse: TypeAlias = List[RepositoryInvitation]
