

from typing import List
from typing_extensions import TypeAlias

from .invitation import Invitation

__all__ = ["InvitationListResponse"]

InvitationListResponse: TypeAlias = List[Invitation]
