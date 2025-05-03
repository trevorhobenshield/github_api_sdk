

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MembershipUpdateParams"]


class MembershipUpdateParams(TypedDict, total=False):
    org: Required[str]

    role: Literal["admin", "member"]
    """The role to give the user in the organization. Can be one of:

    - `admin` - The user will become an owner of the organization.
    - `member` - The user will become a non-owner member of the organization.
    """
