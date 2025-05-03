

from typing import List
from typing_extensions import TypeAlias

from .team import Team

__all__ = ["InvitationListTeamsResponse"]

InvitationListTeamsResponse: TypeAlias = List[Team]
