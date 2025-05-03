

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TeamUpdateParams"]


class TeamUpdateParams(TypedDict, total=False):
    org: Required[str]

    description: str
    """The description of the team."""

    name: str
    """The name of the team."""

    notification_setting: Literal["notifications_enabled", "notifications_disabled"]
    """The notification setting the team has chosen.

    Editing teams without specifying this parameter leaves `notification_setting`
    intact. The options are:

    - `notifications_enabled` - team members receive notifications when the team is
      @mentioned.
    - `notifications_disabled` - no one receives notifications.
    """

    parent_team_id: int | None
    """The ID of a team to set as the parent team."""

    permission: Literal["pull", "push", "admin"]
    """**Closing down notice**.

    The permission that new repositories will be added to the team with when none is
    specified.
    """

    privacy: Literal["secret", "closed"]
    """The level of privacy this team should have.

    Editing teams without specifying this parameter leaves `privacy` intact. When a
    team is nested, the `privacy` for parent teams cannot be `secret`. The options
    are:  
    **For a non-nested team:**

    - `secret` - only visible to organization owners and members of this team.
    - `closed` - visible to all members of this organization.  
      **For a parent or child team:**
    - `closed` - visible to all members of this organization.
    """
