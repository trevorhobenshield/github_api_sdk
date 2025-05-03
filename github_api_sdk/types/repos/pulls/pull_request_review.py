

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...applications.user import User
from ...gists.author_association import AuthorAssociation

__all__ = ["PullRequestReview", "_Links", "_LinksHTML", "_LinksPullRequest"]


class _LinksHTML(BaseModel):
    href: str


class _LinksPullRequest(BaseModel):
    href: str


class _Links(BaseModel):
    html: _LinksHTML

    pull_request: _LinksPullRequest


class PullRequestReview(BaseModel):
    id: int
    """Unique identifier of the review"""

    api_links: _Links = FieldInfo(alias="_links")

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    body: str
    """The text of the review."""

    commit_id: Optional[str] = None
    """A commit SHA for the review.

    If the commit object was garbage collected or forcibly deleted, then it no
    longer exists in Git and this value will be `null`.
    """

    html_url: str

    node_id: str

    pull_request_url: str

    state: str

    user: Optional[User] = None
    """A GitHub user."""

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    submitted_at: Optional[datetime] = None
