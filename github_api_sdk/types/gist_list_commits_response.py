

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .applications.user import User

__all__ = ["GistListCommitsResponse", "GistListCommitsResponseItem", "GistListCommitsResponseItemChangeStatus"]


class GistListCommitsResponseItemChangeStatus(BaseModel):
    additions: Optional[int] = None

    deletions: Optional[int] = None

    total: Optional[int] = None


class GistListCommitsResponseItem(BaseModel):
    change_status: GistListCommitsResponseItemChangeStatus

    committed_at: datetime

    url: str

    user: Optional[User] = None
    """A GitHub user."""

    version: str


GistListCommitsResponse: TypeAlias = List[GistListCommitsResponseItem]
