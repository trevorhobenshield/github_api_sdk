

from typing import List
from typing_extensions import TypeAlias

from .team_simple import TeamSimple

__all__ = ["SecurityManagerListResponse"]

SecurityManagerListResponse: TypeAlias = List[TeamSimple]
