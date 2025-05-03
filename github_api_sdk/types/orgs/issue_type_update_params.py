

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["IssueTypeUpdateParams"]


class IssueTypeUpdateParams(TypedDict, total=False):
    org: Required[str]

    is_enabled: Required[bool]
    """Whether or not the issue type is enabled at the organization level."""

    name: Required[str]
    """Name of the issue type."""

    color: Literal["gray", "blue", "green", "yellow", "orange", "red", "pink", "purple"] | None
    """Color for the issue type."""

    description: str | None
    """Description of the issue type."""
