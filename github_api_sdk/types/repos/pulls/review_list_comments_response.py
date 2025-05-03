

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..link import Link
from ...._models import BaseModel
from ...applications.user import User
from ...gists.author_association import AuthorAssociation
from ...orgs.teams.reaction_rollup import ReactionRollup

__all__ = ["ReviewListCommentsResponse", "ReviewListCommentsResponseItem", "ReviewListCommentsResponseItem_Links"]


class ReviewListCommentsResponseItem_Links(BaseModel):
    html: Link
    """Hypermedia Link"""

    pull_request: Link
    """Hypermedia Link"""

    self: Link
    """Hypermedia Link"""


class ReviewListCommentsResponseItem(BaseModel):
    id: int

    api_links: ReviewListCommentsResponseItem_Links = FieldInfo(alias="_links")

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    body: str

    commit_id: str

    created_at: datetime

    diff_hunk: str

    html_url: str

    node_id: str

    original_commit_id: str

    original_position: int

    path: str

    position: Optional[int] = None

    pull_request_review_id: Optional[int] = None

    pull_request_url: str

    updated_at: datetime

    url: str

    user: Optional[User] = None
    """A GitHub user."""

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    in_reply_to_id: Optional[int] = None

    line: Optional[int] = None
    """The line of the blob to which the comment applies.

    The last line of the range for a multi-line comment
    """

    original_line: Optional[int] = None
    """The original line of the blob to which the comment applies.

    The last line of the range for a multi-line comment
    """

    original_start_line: Optional[int] = None
    """The original first line of the range for a multi-line comment."""

    reactions: Optional[ReactionRollup] = None

    side: Optional[Literal["LEFT", "RIGHT"]] = None
    """The side of the first line of the range for a multi-line comment."""

    start_line: Optional[int] = None
    """The first line of the range for a multi-line comment."""

    start_side: Optional[Literal["LEFT", "RIGHT"]] = None
    """The side of the first line of the range for a multi-line comment."""


ReviewListCommentsResponse: TypeAlias = List[ReviewListCommentsResponseItem]
