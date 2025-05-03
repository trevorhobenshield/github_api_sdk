

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..applications.user import User
from .author_association import AuthorAssociation

__all__ = ["GistComment"]


class GistComment(BaseModel):
    id: int

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    body: str
    """The comment text."""

    created_at: datetime

    node_id: str

    updated_at: datetime

    url: str

    user: Optional[User] = None
    """A GitHub user."""
