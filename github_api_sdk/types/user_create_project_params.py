

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserCreateProjectParams"]


class UserCreateProjectParams(TypedDict, total=False):
    name: Required[str]
    """Name of the project"""

    body: str | None
    """Body of the project"""
