

from typing import List
from typing_extensions import TypeAlias

from .....orgs.team import Team

__all__ = ["TeamRemoveResponse"]

TeamRemoveResponse: TypeAlias = List[Team]
