

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["GistUpdateParams", "Files"]


class GistUpdateParams(TypedDict, total=False):
    description: str
    """The description of the gist."""

    files: dict[str, Files | None]
    """The gist files to be updated, renamed, or deleted.

    Each `key` must match the current filename (including extension) of the targeted
    gist file. For example: `hello.py`.

    To delete a file, set the whole file to null. For example: `hello.py : null`.
    The file will also be deleted if the specified object does not contain at least
    one of `content` or `filename`.
    """


class Files(TypedDict, total=False):
    content: str
    """The new content of the file."""

    filename: str | None
    """The new filename for the file."""
