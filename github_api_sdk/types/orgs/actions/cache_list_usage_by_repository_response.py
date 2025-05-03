

from typing import List

from ...._models import BaseModel
from ...repos.actions.actions_cache_usage import ActionsCacheUsage

__all__ = ["CacheListUsageByRepositoryResponse"]


class CacheListUsageByRepositoryResponse(BaseModel):
    repository_cache_usages: List[ActionsCacheUsage]

    total_count: int
