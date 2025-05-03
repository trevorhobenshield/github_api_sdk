

from typing import Optional
from datetime import datetime

from ....._models import BaseModel
from ..reaction_rollup import ReactionRollup
from ....applications.user import User

__all__ = ["TeamDiscussionComment"]


class TeamDiscussionComment(BaseModel):
    author: Optional[User] = None
    """A GitHub user."""

    body: str
    """The main text of the comment."""

    body_html: str

    body_version: str
    """The current version of the body content.

    If provided, this update operation will be rejected if the given version does
    not match the latest version on the server.
    """

    created_at: datetime

    discussion_url: str

    html_url: str

    last_edited_at: Optional[datetime] = None

    node_id: str

    number: int
    """The unique sequence number of a team discussion comment."""

    updated_at: datetime

    url: str

    reactions: Optional[ReactionRollup] = None
