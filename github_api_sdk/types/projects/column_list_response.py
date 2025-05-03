

from typing import List
from typing_extensions import TypeAlias

from .project_column import ProjectColumn

__all__ = ["ColumnListResponse"]

ColumnListResponse: TypeAlias = List[ProjectColumn]
