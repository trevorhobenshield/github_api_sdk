

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepoAddOrUpdatePermissionsParams"]


class RepoAddOrUpdatePermissionsParams(TypedDict, total=False):
    team_id: Required[int]

    owner: Required[str]

    permission: Literal["pull", "push", "admin"]
    """The permission to grant the team on this repository.

    If no permission is specified, the team's `permission` attribute will be used to
    determine what permission to grant the team on this repository.
    """
