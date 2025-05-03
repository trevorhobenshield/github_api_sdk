

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProjectCreateParams"]


class ProjectCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the project."""

    body: str
    """The description of the project."""
