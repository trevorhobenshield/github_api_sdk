

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContentCreateOrUpdateParams", "Author", "Committer"]


class ContentCreateOrUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    content: Required[str]
    """The new file content, using Base64 encoding."""

    message: Required[str]
    """The commit message."""

    author: Author
    """The author of the file.

    Default: The `committer` or the authenticated user if you omit `committer`.
    """

    branch: str
    """The branch name. Default: the repository’s default branch."""

    committer: Committer
    """The person that committed the file. Default: the authenticated user."""

    sha: str
    """**Required if you are updating a file**.

    The blob SHA of the file being replaced.
    """


class Author(TypedDict, total=False):
    email: Required[str]
    """The email of the author or committer of the commit.

    You'll receive a `422` status code if `email` is omitted.
    """

    name: Required[str]
    """The name of the author or committer of the commit.

    You'll receive a `422` status code if `name` is omitted.
    """

    date: str


class Committer(TypedDict, total=False):
    email: Required[str]
    """The email of the author or committer of the commit.

    You'll receive a `422` status code if `email` is omitted.
    """

    name: Required[str]
    """The name of the author or committer of the commit.

    You'll receive a `422` status code if `name` is omitted.
    """

    date: str
