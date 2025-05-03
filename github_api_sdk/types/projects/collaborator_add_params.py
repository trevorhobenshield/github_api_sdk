

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollaboratorAddParams"]


class CollaboratorAddParams(TypedDict, total=False):
    project_id: Required[int]

    permission: Literal["read", "write", "admin"]
    """The permission to grant the collaborator."""
