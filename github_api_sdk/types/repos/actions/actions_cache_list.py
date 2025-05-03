

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ActionsCacheList", "ActionsCach"]


class ActionsCach(BaseModel):
    id: Optional[int] = None

    created_at: Optional[datetime] = None

    key: Optional[str] = None

    last_accessed_at: Optional[datetime] = None

    ref: Optional[str] = None

    size_in_bytes: Optional[int] = None

    version: Optional[str] = None


class ActionsCacheList(BaseModel):
    actions_caches: List[ActionsCach]
    """Array of caches"""

    total_count: int
    """Total number of caches"""
