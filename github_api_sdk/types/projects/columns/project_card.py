

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ...applications.user import User

__all__ = ["ProjectCard"]


class ProjectCard(BaseModel):
    id: int
    """The project card's ID"""

    column_url: str

    created_at: datetime

    creator: Optional[User] = None
    """A GitHub user."""

    node_id: str

    note: Optional[str] = None

    project_url: str

    updated_at: datetime

    url: str

    archived: Optional[bool] = None
    """Whether or not the card is archived"""

    column_name: Optional[str] = None

    content_url: Optional[str] = None

    project_id: Optional[str] = None
