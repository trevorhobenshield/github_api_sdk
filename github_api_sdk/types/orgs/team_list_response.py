

from typing import List
from typing_extensions import TypeAlias

from .team import Team

__all__ = ["TeamListResponse"]

TeamListResponse: TypeAlias = List[Team]
