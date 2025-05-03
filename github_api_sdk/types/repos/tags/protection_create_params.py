

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProtectionCreateParams"]


class ProtectionCreateParams(TypedDict, total=False):
    owner: Required[str]

    pattern: Required[str]
    """An optional glob pattern to match against when enforcing tag protection."""
