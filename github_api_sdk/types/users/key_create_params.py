

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    key: Required[str]
    """The public SSH key to add to your GitHub account."""

    title: str
    """A descriptive name for the new key."""
