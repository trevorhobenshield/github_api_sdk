

from typing import List
from typing_extensions import TypeAlias

from ..orgs.project import Project

__all__ = ["ProjectListResponse"]

ProjectListResponse: TypeAlias = List[Project]
