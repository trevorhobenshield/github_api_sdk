

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RepoUpdateParams"]


class RepoUpdateParams(TypedDict, total=False):
    org: Required[str]

    team_slug: Required[str]

    owner: Required[str]

    permission: str
    """The permission to grant the team on this repository.

    We accept the following permissions to be set: `pull`, `triage`, `push`,
    `maintain`, `admin` and you can also specify a custom repository role name, if
    the owning organization has defined any. If no permission is specified, the
    team's `permission` attribute will be used to determine what permission to grant
    the team on this repository.
    """
