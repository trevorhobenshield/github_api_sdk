

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SelectedTeamAddParams"]


class SelectedTeamAddParams(TypedDict, total=False):
    selected_teams: Required[list[str]]
    """
    List of team names within the organization to which to grant access to GitHub
    Copilot.
    """
