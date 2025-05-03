

from typing import List
from typing_extensions import TypeAlias

from .team_project import TeamProject

__all__ = ["ProjectListResponse"]

ProjectListResponse: TypeAlias = List[TeamProject]
