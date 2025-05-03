


from ...._models import BaseModel

__all__ = ["ActionsCacheUsage"]


class ActionsCacheUsage(BaseModel):
    active_caches_count: int
    """The number of active caches in the repository."""

    active_caches_size_in_bytes: int
    """The sum of the size in bytes of all the active cache items in the repository."""

    full_name: str
    """The repository owner and name for the cache usage being shown."""
