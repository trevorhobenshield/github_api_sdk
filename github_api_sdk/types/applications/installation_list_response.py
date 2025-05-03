

from typing import List
from typing_extensions import TypeAlias

from .installation import Installation

__all__ = ["InstallationListResponse"]

InstallationListResponse: TypeAlias = List[Installation]
