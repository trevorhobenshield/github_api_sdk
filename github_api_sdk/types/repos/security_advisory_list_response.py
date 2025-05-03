

from typing import List
from typing_extensions import TypeAlias

from .repository_advisory import RepositoryAdvisory

__all__ = ["SecurityAdvisoryListResponse"]

SecurityAdvisoryListResponse: TypeAlias = List[RepositoryAdvisory]
