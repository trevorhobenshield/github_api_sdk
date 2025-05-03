

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SelectedUserRemoveParams"]


class SelectedUserRemoveParams(TypedDict, total=False):
    selected_usernames: Required[list[str]]
    """
    The usernames of the organization members whose codespaces should not be billed
    to the organization.
    """
