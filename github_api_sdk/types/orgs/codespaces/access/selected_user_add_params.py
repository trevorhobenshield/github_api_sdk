

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SelectedUserAddParams"]


class SelectedUserAddParams(TypedDict, total=False):
    selected_usernames: Required[list[str]]
    """
    The usernames of the organization members whose codespaces be billed to the
    organization.
    """
