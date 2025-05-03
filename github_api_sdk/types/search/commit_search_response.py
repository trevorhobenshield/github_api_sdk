

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..applications.user import User
from ..nullable_git_user import NullableGitUser
from ..minimal_repository import MinimalRepository
from ..repos.git.verification import Verification
from ..search_result_text_match import SearchResultTextMatch

__all__ = ["CommitSearchResponse", "Item", "ItemCommit", "ItemCommitAuthor", "ItemCommitTree", "ItemParent"]


class ItemCommitAuthor(BaseModel):
    date: datetime

    email: str

    name: str


class ItemCommitTree(BaseModel):
    sha: str

    url: str


class ItemCommit(BaseModel):
    author: ItemCommitAuthor

    comment_count: int

    committer: Optional[NullableGitUser] = None
    """Metaproperties for Git author/committer information."""

    message: str

    tree: ItemCommitTree

    url: str

    verification: Optional[Verification] = None


class ItemParent(BaseModel):
    html_url: Optional[str] = None

    sha: Optional[str] = None

    url: Optional[str] = None


class Item(BaseModel):
    author: Optional[User] = None
    """A GitHub user."""

    comments_url: str

    commit: ItemCommit

    committer: Optional[NullableGitUser] = None
    """Metaproperties for Git author/committer information."""

    html_url: str

    node_id: str

    parents: List[ItemParent]

    repository: MinimalRepository
    """Minimal Repository"""

    score: float

    sha: str

    url: str

    text_matches: Optional[List[SearchResultTextMatch]] = None


class CommitSearchResponse(BaseModel):
    incomplete_results: bool

    items: List[Item]

    total_count: int
