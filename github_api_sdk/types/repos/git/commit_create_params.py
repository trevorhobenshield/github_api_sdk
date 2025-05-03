

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CommitCreateParams", "Author", "Committer"]


class CommitCreateParams(TypedDict, total=False):
    owner: Required[str]

    message: Required[str]
    """The commit message"""

    tree: Required[str]
    """The SHA of the tree object this commit points to"""

    author: Author
    """Information about the author of the commit.

    By default, the `author` will be the authenticated user and the current date.
    See the `author` and `committer` object below for details.
    """

    committer: Committer
    """Information about the person who is making the commit.

    By default, `committer` will use the information set in `author`. See the
    `author` and `committer` object below for details.
    """

    parents: list[str]
    """The full SHAs of the commits that were the parents of this commit.

    If omitted or empty, the commit will be written as a root commit. For a single
    parent, an array of one SHA should be provided; for a merge commit, an array of
    more than one should be provided.
    """

    signature: str
    """
    The [PGP signature](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) of the
    commit. GitHub adds the signature to the `gpgsig` header of the created commit.
    For a commit signature to be verifiable by Git or GitHub, it must be an
    ASCII-armored detached PGP signature over the string commit as it would be
    written to the object database. To pass a `signature` parameter, you need to
    first manually create a valid PGP signature, which can be complicated. You may
    find it easier to
    [use the command line](https://git-scm.com/book/id/v2/Git-Tools-Signing-Your-Work)
    to create signed commits.
    """


class Author(TypedDict, total=False):
    email: Required[str]
    """The email of the author (or committer) of the commit"""

    name: Required[str]
    """The name of the author (or committer) of the commit"""

    date: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Indicates when this commit was authored (or committed).

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """


class Committer(TypedDict, total=False):
    date: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Indicates when this commit was authored (or committed).

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    email: str
    """The email of the author (or committer) of the commit"""

    name: str
    """The name of the author (or committer) of the commit"""
