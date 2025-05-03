

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContentDeleteParams", "Author", "Committer"]


class ContentDeleteParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    message: Required[str]
    """The commit message."""

    sha: Required[str]
    """The blob SHA of the file being deleted."""

    author: Author
    """object containing information about the author."""

    branch: str
    """The branch name. Default: the repository’s default branch"""

    committer: Committer
    """object containing information about the committer."""


class Author(TypedDict, total=False):
    email: str
    """The email of the author (or committer) of the commit"""

    name: str
    """The name of the author (or committer) of the commit"""


class Committer(TypedDict, total=False):
    email: str
    """The email of the author (or committer) of the commit"""

    name: str
    """The name of the author (or committer) of the commit"""
