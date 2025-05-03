

from typing import List
from typing_extensions import TypeAlias

from ..orgs.teams.team_project import TeamProject

__all__ = ["ProjectListResponse"]

ProjectListResponse: TypeAlias = List[TeamProject]
