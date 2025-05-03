

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccessUpdateParams"]


class AccessUpdateParams(TypedDict, total=False):
    visibility: Required[
        Literal["disabled", "selected_members", "all_members", "all_members_and_outside_collaborators"]
    ]
    """Which users can access codespaces in the organization.

    `disabled` means that no users can access codespaces in the organization.
    """

    selected_usernames: list[str]
    """
    The usernames of the organization members who should have access to codespaces
    in the organization. Required when `visibility` is `selected_members`. The
    provided list of usernames will replace any existing value.
    """
