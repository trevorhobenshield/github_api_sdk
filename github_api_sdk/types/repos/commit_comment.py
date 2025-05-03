

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..applications.user import User
from ..gists.author_association import AuthorAssociation
from ..orgs.teams.reaction_rollup import ReactionRollup

__all__ = ["CommitComment"]


class CommitComment(BaseModel):
    id: int

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    body: str

    commit_id: str

    created_at: datetime

    html_url: str

    line: Optional[int] = None

    node_id: str

    path: Optional[str] = None

    position: Optional[int] = None

    updated_at: datetime

    url: str

    user: Optional[User] = None
    """A GitHub user."""

    reactions: Optional[ReactionRollup] = None
