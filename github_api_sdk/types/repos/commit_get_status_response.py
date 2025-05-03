

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..minimal_repository import MinimalRepository

__all__ = ["CommitGetStatusResponse", "Status"]


class Status(BaseModel):
    id: int

    avatar_url: Optional[str] = None

    context: str

    created_at: datetime

    description: Optional[str] = None

    node_id: str

    state: str

    target_url: Optional[str] = None

    updated_at: datetime

    url: str

    required: Optional[bool] = None


class CommitGetStatusResponse(BaseModel):
    commit_url: str

    repository: MinimalRepository
    """Minimal Repository"""

    sha: str

    state: str

    statuses: List[Status]

    total_count: int

    url: str
