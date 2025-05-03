

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InvitationUpdateParams"]


class InvitationUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    permissions: Literal["read", "write", "maintain", "triage", "admin"]
    """The permissions that the associated user will have on the repository.

    Valid values are `read`, `write`, `maintain`, `triage`, and `admin`.
    """
