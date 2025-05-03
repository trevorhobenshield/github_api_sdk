

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..orgs.simple_user import SimpleUser
from ..applications.user import User

__all__ = ["BaseGist", "Files"]


class Files(BaseModel):
    encoding: Optional[str] = None
    """The encoding used for `content`.

    Currently, `"utf-8"` and `"base64"` are supported.
    """

    filename: Optional[str] = None

    language: Optional[str] = None

    raw_url: Optional[str] = None

    size: Optional[int] = None

    type: Optional[str] = None


class BaseGist(BaseModel):
    id: str

    comments: int

    comments_url: str

    commits_url: str

    created_at: datetime

    description: Optional[str] = None

    files: Dict[str, Files]

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

    owner: Optional[SimpleUser] = None
    """A GitHub user."""

    truncated: Optional[bool] = None
