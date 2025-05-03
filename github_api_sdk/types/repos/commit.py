
from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .diff_entry import DiffEntry
from ..orgs.simple_user import SimpleUser

__all__ = ["Commit", "Author", "Committer", "Parent", "Stats"]

Author: TypeAlias = Union[SimpleUser, object, None]

Committer: TypeAlias = Union[SimpleUser, object, None]


class Parent(BaseModel):
    sha: str

    url: str

    html_url: str | None = None


class Stats(BaseModel):
    additions: int | None = None

    deletions: int | None = None

    total: int | None = None


class Commit(BaseModel):
    author: Author | None = None
    """A GitHub user."""

    comments_url: str

    commit: Commit

    committer: Committer | None = None
    """A GitHub user."""

    html_url: str

    node_id: str

    parents: list[Parent]

    sha: str

    url: str

    files: list[DiffEntry] | None = None

    stats: Stats | None = None
