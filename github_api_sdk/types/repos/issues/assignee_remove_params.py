

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AssigneeRemoveParams"]


class AssigneeRemoveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    assignees: list[str]
    """Usernames of assignees to remove from an issue.

    _NOTE: Only users with push access can remove assignees from an issue. Assignees
    are silently ignored otherwise._
    """
