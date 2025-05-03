

from typing import List
from typing_extensions import TypeAlias

from ..repos.repository_invitation import RepositoryInvitation

__all__ = ["RepositoryInvitationListResponse"]

RepositoryInvitationListResponse: TypeAlias = List[RepositoryInvitation]
