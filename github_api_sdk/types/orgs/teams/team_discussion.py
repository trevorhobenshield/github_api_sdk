

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .reaction_rollup import ReactionRollup
from ...applications.user import User

__all__ = ["TeamDiscussion"]


class TeamDiscussion(BaseModel):
    author: Optional[User] = None
    """A GitHub user."""

    body: str
    """The main text of the discussion."""

    body_html: str

    body_version: str
    """The current version of the body content.

    If provided, this update operation will be rejected if the given version does
    not match the latest version on the server.
    """

    comments_count: int

    comments_url: str

    created_at: datetime

    html_url: str

    last_edited_at: Optional[datetime] = None

    node_id: str

    number: int
    """The unique sequence number of a team discussion."""

    pinned: bool
    """Whether or not this discussion should be pinned for easy retrieval."""

    private: bool
    """
    Whether or not this discussion should be restricted to team members and
    organization owners.
    """

    team_url: str

    title: str
    """The title of the discussion."""

    updated_at: datetime

    url: str

    reactions: Optional[ReactionRollup] = None
