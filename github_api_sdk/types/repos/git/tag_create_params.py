

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TagCreateParams", "Tagger"]


class TagCreateParams(TypedDict, total=False):
    owner: Required[str]

    message: Required[str]
    """The tag message."""

    object: Required[str]
    """The SHA of the git object this is tagging."""

    tag: Required[str]
    """The tag's name. This is typically a version (e.g., "v0.0.1")."""

    type: Required[Literal["commit", "tree", "blob"]]
    """The type of the object we're tagging.

    Normally this is a `commit` but it can also be a `tree` or a `blob`.
    """

    tagger: Tagger
    """An object with information about the individual creating the tag."""


class Tagger(TypedDict, total=False):
    email: Required[str]
    """The email of the author of the tag"""

    name: Required[str]
    """The name of the author of the tag"""

    date: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """When this object was tagged.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """
