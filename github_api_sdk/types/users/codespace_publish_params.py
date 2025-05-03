

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CodespacePublishParams"]


class CodespacePublishParams(TypedDict, total=False):
    name: str
    """A name for the new repository."""

    private: bool
    """Whether the new repository should be private."""
