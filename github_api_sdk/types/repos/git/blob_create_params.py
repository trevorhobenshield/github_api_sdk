

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BlobCreateParams"]


class BlobCreateParams(TypedDict, total=False):
    owner: Required[str]

    content: Required[str]
    """The new blob's content."""

    encoding: str
    """The encoding used for `content`.

    Currently, `"utf-8"` and `"base64"` are supported.
    """
