

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MembershipUpdateParams"]


class MembershipUpdateParams(TypedDict, total=False):
    org: Required[str]

    team_slug: Required[str]

    role: Literal["member", "maintainer"]
    """The role that this user should have in the team."""
