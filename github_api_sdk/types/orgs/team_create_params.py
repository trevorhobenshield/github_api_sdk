

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TeamCreateParams"]


class TeamCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the team."""

    description: str
    """The description of the team."""

    maintainers: list[str]
    """List GitHub IDs for organization members who will become team maintainers."""

    notification_setting: Literal["notifications_enabled", "notifications_disabled"]
    """The notification setting the team has chosen. The options are:

    - `notifications_enabled` - team members receive notifications when the team is
      @mentioned.
    - `notifications_disabled` - no one receives notifications.  
      Default: `notifications_enabled`
    """

    parent_team_id: int
    """The ID of a team to set as the parent team."""

    permission: Literal["pull", "push"]
    """**Closing down notice**.

    The permission that new repositories will be added to the team with when none is
    specified.
    """

    privacy: Literal["secret", "closed"]
    """The level of privacy this team should have.

    The options are:  
    **For a non-nested team:**

    - `secret` - only visible to organization owners and members of this team.
    - `closed` - visible to all members of this organization.  
      Default: `secret`  
      **For a parent or child team:**
    - `closed` - visible to all members of this organization.  
      Default for child team: `closed`
    """

    repo_names: list[str]
    """
    The full name (e.g., "organization-name/repository-name") of repositories to add
    the team to.
    """
