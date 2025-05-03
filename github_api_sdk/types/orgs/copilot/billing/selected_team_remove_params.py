

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SelectedTeamRemoveParams"]


class SelectedTeamRemoveParams(TypedDict, total=False):
    selected_teams: Required[list[str]]
    """The names of teams from which to revoke access to GitHub Copilot."""
