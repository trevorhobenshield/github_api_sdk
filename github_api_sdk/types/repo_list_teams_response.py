

from typing import List
from typing_extensions import TypeAlias

from .orgs.team import Team

__all__ = ["RepoListTeamsResponse"]

RepoListTeamsResponse: TypeAlias = List[Team]
