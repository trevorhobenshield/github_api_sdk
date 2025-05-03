

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FileCommit",
    "Commit",
    "CommitAuthor",
    "CommitCommitter",
    "CommitParent",
    "CommitTree",
    "CommitVerification",
    "Content",
    "Content_Links",
]


class CommitAuthor(BaseModel):
    date: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None


class CommitCommitter(BaseModel):
    date: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None


class CommitParent(BaseModel):
    html_url: Optional[str] = None

    sha: Optional[str] = None

    url: Optional[str] = None


class CommitTree(BaseModel):
    sha: Optional[str] = None

    url: Optional[str] = None


class CommitVerification(BaseModel):
    payload: Optional[str] = None

    reason: Optional[str] = None

    signature: Optional[str] = None

    verified: Optional[bool] = None

    verified_at: Optional[str] = None


class Commit(BaseModel):
    author: Optional[CommitAuthor] = None

    committer: Optional[CommitCommitter] = None

    html_url: Optional[str] = None

    message: Optional[str] = None

    node_id: Optional[str] = None

    parents: Optional[List[CommitParent]] = None

    sha: Optional[str] = None

    tree: Optional[CommitTree] = None

    url: Optional[str] = None

    verification: Optional[CommitVerification] = None


class Content_Links(BaseModel):
    git: Optional[str] = None

    html: Optional[str] = None

    self: Optional[str] = None


class Content(BaseModel):
    api_links: Optional[Content_Links] = FieldInfo(alias="_links", default=None)

    download_url: Optional[str] = None

    git_url: Optional[str] = None

    html_url: Optional[str] = None

    name: Optional[str] = None

    path: Optional[str] = None

    sha: Optional[str] = None

    size: Optional[int] = None

    type: Optional[str] = None

    url: Optional[str] = None


class FileCommit(BaseModel):
    commit: Commit

    content: Optional[Content] = None
