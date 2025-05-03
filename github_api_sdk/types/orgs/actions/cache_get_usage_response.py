


from ...._models import BaseModel

__all__ = ["CacheGetUsageResponse"]


class CacheGetUsageResponse(BaseModel):
    total_active_caches_count: int
    """
    The count of active caches across all repositories of an enterprise or an
    organization.
    """

    total_active_caches_size_in_bytes: int
    """
    The total size in bytes of all active cache items across all repositories of an
    enterprise or an organization.
    """
