

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["GitCommit", "Author", "Committer", "Parent", "Tree", "Verification"]


class Author(BaseModel):
    date: datetime
    """Timestamp of the commit"""

    email: str
    """Git email address of the user"""

    name: str
    """Name of the git user"""


class Committer(BaseModel):
    date: datetime
    """Timestamp of the commit"""

    email: str
    """Git email address of the user"""

    name: str
    """Name of the git user"""


class Parent(BaseModel):
    html_url: str

    sha: str
    """SHA for the commit"""

    url: str


class Tree(BaseModel):
    sha: str
    """SHA for the commit"""

    url: str


class Verification(BaseModel):
    payload: Optional[str] = None

    reason: str

    signature: Optional[str] = None

    verified: bool

    verified_at: Optional[str] = None


class GitCommit(BaseModel):
    author: Author
    """Identifying information for the git-user"""

    committer: Committer
    """Identifying information for the git-user"""

    html_url: str

    message: str
    """Message describing the purpose of the commit"""

    node_id: str

    parents: List[Parent]

    sha: str
    """SHA for the commit"""

    tree: Tree

    url: str

    verification: Verification
