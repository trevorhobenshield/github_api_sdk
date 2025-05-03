

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .public_user import PublicUser
from .orgs.simple_user import SimpleUser
from .applications.user import User

__all__ = ["GistSimple", "Files", "ForkOf", "ForkOfFiles", "Fork", "History", "HistoryChangeStatus"]


class Files(BaseModel):
    content: Optional[str] = None

    encoding: Optional[str] = None
    """The encoding used for `content`.

    Currently, `"utf-8"` and `"base64"` are supported.
    """

    filename: Optional[str] = None

    language: Optional[str] = None

    raw_url: Optional[str] = None

    size: Optional[int] = None

    truncated: Optional[bool] = None

    type: Optional[str] = None


class ForkOfFiles(BaseModel):
    filename: Optional[str] = None

    language: Optional[str] = None

    raw_url: Optional[str] = None

    size: Optional[int] = None

    type: Optional[str] = None


class ForkOf(BaseModel):
    id: str

    comments: int

    comments_url: str

    commits_url: str

    created_at: datetime

    description: Optional[str] = None

    files: Dict[str, ForkOfFiles]

    forks_url: str

    git_pull_url: str

    git_push_url: str

    html_url: str

    node_id: str

    public: bool

    updated_at: datetime

    url: str

    user: Optional[User] = None
    """A GitHub user."""

    comments_enabled: Optional[bool] = None

    forks: Optional[List[object]] = None

    history: Optional[List[object]] = None

    owner: Optional[User] = None
    """A GitHub user."""

    truncated: Optional[bool] = None


class Fork(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None

    user: Optional[PublicUser] = None
    """Public User"""


class HistoryChangeStatus(BaseModel):
    additions: Optional[int] = None

    deletions: Optional[int] = None

    total: Optional[int] = None


class History(BaseModel):
    change_status: Optional[HistoryChangeStatus] = None

    committed_at: Optional[datetime] = None

    url: Optional[str] = None

    user: Optional[User] = None
    """A GitHub user."""

    version: Optional[str] = None


class GistSimple(BaseModel):
    id: Optional[str] = None

    comments: Optional[int] = None

    comments_enabled: Optional[bool] = None

    comments_url: Optional[str] = None

    commits_url: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    files: Optional[Dict[str, Optional[Files]]] = None

    fork_of: Optional[ForkOf] = None
    """Gist"""

    forks: Optional[List[Fork]] = None

    forks_url: Optional[str] = None

    git_pull_url: Optional[str] = None

    git_push_url: Optional[str] = None

    history: Optional[List[History]] = None

    html_url: Optional[str] = None

    node_id: Optional[str] = None

    owner: Optional[SimpleUser] = None
    """A GitHub user."""

    public: Optional[bool] = None

    truncated: Optional[bool] = None

    updated_at: Optional[str] = None

    url: Optional[str] = None

    user: Optional[str] = None
