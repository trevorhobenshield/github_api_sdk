

from typing import List
from typing_extensions import TypeAlias

from .orgs.team import Team

__all__ = ["TeamListChildTeamsResponse"]

TeamListChildTeamsResponse: TypeAlias = List[Team]
