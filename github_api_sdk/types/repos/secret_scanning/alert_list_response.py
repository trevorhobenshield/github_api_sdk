

from typing import List
from typing_extensions import TypeAlias

from .repo_alert import RepoAlert

__all__ = ["AlertListResponse"]

AlertListResponse: TypeAlias = List[RepoAlert]
