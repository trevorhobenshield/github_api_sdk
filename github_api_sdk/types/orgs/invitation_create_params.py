

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["InvitationCreateParams"]


class InvitationCreateParams(TypedDict, total=False):
    email: str
    """**Required unless you provide `invitee_id`**.

    Email address of the person you are inviting, which can be an existing GitHub
    user.
    """

    invitee_id: int
    """**Required unless you provide `email`**.

    GitHub user ID for the person you are inviting.
    """

    role: Literal["admin", "direct_member", "billing_manager", "reinstate"]
    """The role for the new member.

    - `admin` - Organization owners with full administrative rights to the
      organization and complete access to all repositories and teams.
    - `direct_member` - Non-owner organization members with ability to see other
      members and join teams by invitation.
    - `billing_manager` - Non-owner organization members with ability to manage the
      billing settings of your organization.
    - `reinstate` - The previous role assigned to the invitee before they were
      removed from your organization. Can be one of the roles listed above. Only
      works if the invitee was previously part of your organization.
    """

    team_ids: Iterable[int]
    """Specify IDs for the teams you want to invite new members to."""
