

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ...applications.user import User

__all__ = ["PageBuild", "Error"]


class Error(BaseModel):
    message: Optional[str] = None


class PageBuild(BaseModel):
    commit: str

    created_at: datetime

    duration: int

    error: Error

    pusher: Optional[User] = None
    """A GitHub user."""

    status: str

    updated_at: datetime

    url: str
