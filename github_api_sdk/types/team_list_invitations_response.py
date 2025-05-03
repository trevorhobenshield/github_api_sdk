

from typing import List
from typing_extensions import TypeAlias

from .orgs.invitation import Invitation

__all__ = ["TeamListInvitationsResponse"]

TeamListInvitationsResponse: TypeAlias = List[Invitation]
