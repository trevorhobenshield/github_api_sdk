

from typing import List
from typing_extensions import TypeAlias

from .orgs.team_full import TeamFull

__all__ = ["UserListTeamsResponse"]

UserListTeamsResponse: TypeAlias = List[TeamFull]
