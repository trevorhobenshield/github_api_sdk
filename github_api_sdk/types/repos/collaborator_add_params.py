

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CollaboratorAddParams"]


class CollaboratorAddParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    permission: str
    """The permission to grant the collaborator.

    **Only valid on organization-owned repositories.** We accept the following
    permissions to be set: `pull`, `triage`, `push`, `maintain`, `admin` and you can
    also specify a custom repository role name, if the owning organization has
    defined any.
    """
