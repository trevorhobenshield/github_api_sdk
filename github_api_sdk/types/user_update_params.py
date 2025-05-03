

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    bio: str
    """The new short biography of the user."""

    blog: str
    """The new blog URL of the user."""

    company: str
    """The new company of the user."""

    email: str
    """The publicly visible email address of the user."""

    hireable: bool
    """The new hiring availability of the user."""

    location: str
    """The new location of the user."""

    name: str
    """The new name of the user."""

    twitter_username: str | None
    """The new Twitter username of the user."""
