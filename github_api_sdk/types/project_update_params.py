

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    body: str | None
    """Body of the project"""

    name: str
    """Name of the project"""

    organization_permission: Literal["read", "write", "admin", "none"]
    """The baseline permission that all organization members have on this project"""

    private: bool
    """Whether or not this project can be seen by everyone."""

    state: str
    """State of the project; either 'open' or 'closed'"""
