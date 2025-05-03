

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...orgs.simple_user import SimpleUser
from ...gists.author_association import AuthorAssociation
from ...orgs.teams.reaction_rollup import ReactionRollup

__all__ = ["PullRequestReviewComment", "_Links", "_LinksHTML", "_LinksPullRequest", "_LinksSelf"]


class _LinksHTML(BaseModel):
    href: str


class _LinksPullRequest(BaseModel):
    href: str


class _LinksSelf(BaseModel):
    href: str


class _Links(BaseModel):
    html: _LinksHTML

    pull_request: _LinksPullRequest

    self: _LinksSelf


class PullRequestReviewComment(BaseModel):
    id: int
    """The ID of the pull request review comment."""

    api_links: _Links = FieldInfo(alias="_links")

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    body: str
    """The text of the comment."""

    commit_id: str
    """The SHA of the commit to which the comment applies."""

    created_at: datetime

    diff_hunk: str
    """The diff of the line that the comment refers to."""

    html_url: str
    """HTML URL for the pull request review comment."""

    node_id: str
    """The node ID of the pull request review comment."""

    original_commit_id: str
    """The SHA of the original commit to which the comment applies."""

    path: str
    """The relative path of the file to which the comment applies."""

    pull_request_review_id: Optional[int] = None
    """The ID of the pull request review to which the comment belongs."""

    pull_request_url: str
    """URL for the pull request that the review comment belongs to."""

    updated_at: datetime

    url: str
    """URL for the pull request review comment"""

    user: SimpleUser
    """A GitHub user."""

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    in_reply_to_id: Optional[int] = None
    """The comment ID to reply to."""

    line: Optional[int] = None
    """The line of the blob to which the comment applies.

    The last line of the range for a multi-line comment
    """

    original_line: Optional[int] = None
    """The line of the blob to which the comment applies.

    The last line of the range for a multi-line comment
    """

    original_position: Optional[int] = None
    """The index of the original line in the diff to which the comment applies.

    This field is closing down; use `original_line` instead.
    """

    original_start_line: Optional[int] = None
    """The first line of the range for a multi-line comment."""

    position: Optional[int] = None
    """The line index in the diff to which the comment applies.

    This field is closing down; use `line` instead.
    """

    reactions: Optional[ReactionRollup] = None

    side: Optional[Literal["LEFT", "RIGHT"]] = None
    """The side of the diff to which the comment applies.

    The side of the last line of the range for a multi-line comment
    """

    start_line: Optional[int] = None
    """The first line of the range for a multi-line comment."""

    start_side: Optional[Literal["LEFT", "RIGHT"]] = None
    """The side of the first line of the range for a multi-line comment."""

    subject_type: Optional[Literal["line", "file"]] = None
    """The level at which the comment is targeted, can be a diff line or a file."""
