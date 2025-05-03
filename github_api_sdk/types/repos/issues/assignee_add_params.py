

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AssigneeAddParams"]


class AssigneeAddParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    assignees: list[str]
    """Usernames of people to assign this issue to.

    _NOTE: Only users with push access can add assignees to an issue. Assignees are
    silently ignored otherwise._
    """
