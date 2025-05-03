

from typing import List
from typing_extensions import TypeAlias

from .team import Team

__all__ = ["TeamListChildTeamsResponse"]

TeamListChildTeamsResponse: TypeAlias = List[Team]
