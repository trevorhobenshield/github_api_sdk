

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["UserRemoveParams"]


class UserRemoveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    users: Required[list[str]]
    """The username for users"""
