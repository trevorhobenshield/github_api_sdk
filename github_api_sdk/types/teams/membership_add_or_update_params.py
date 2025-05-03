

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MembershipAddOrUpdateParams"]


class MembershipAddOrUpdateParams(TypedDict, total=False):
    team_id: Required[int]

    role: Literal["member", "maintainer"]
    """The role that this user should have in the team."""
