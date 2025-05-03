

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GpgKeyCreateParams"]


class GpgKeyCreateParams(TypedDict, total=False):
    armored_public_key: Required[str]
    """A GPG key in ASCII-armored format."""

    name: str
    """A descriptive name for the new key."""
