

from typing import Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from .team import Team
from ..._models import BaseModel
from .simple_user import SimpleUser

__all__ = ["CopilotSeatDetails", "AssigningTeam", "AssigningTeamEnterpriseTeam", "Organization"]


class AssigningTeamEnterpriseTeam(BaseModel):
    id: int

    created_at: datetime

    html_url: str

    members_url: str

    name: str

    slug: str

    sync_to_organizations: str

    updated_at: datetime

    url: str

    group_id: Optional[str] = None

    group_name: Optional[str] = None


AssigningTeam: TypeAlias = Union[Team, AssigningTeamEnterpriseTeam, None]


class Organization(BaseModel):
    id: int

    avatar_url: str

    description: Optional[str] = None

    events_url: str

    hooks_url: str

    issues_url: str

    login: str

    members_url: str

    node_id: str

    public_members_url: str

    repos_url: str

    url: str


class CopilotSeatDetails(BaseModel):
    assignee: SimpleUser
    """A GitHub user."""

    created_at: datetime
    """
    Timestamp of when the assignee was last granted access to GitHub Copilot, in ISO
    8601 format.
    """

    assigning_team: Optional[AssigningTeam] = None
    """
    The team through which the assignee is granted access to GitHub Copilot, if
    applicable.
    """

    last_activity_at: Optional[datetime] = None
    """Timestamp of user's last GitHub Copilot activity, in ISO 8601 format."""

    last_activity_editor: Optional[str] = None
    """Last editor that was used by the user for a GitHub Copilot completion."""

    organization: Optional[Organization] = None
    """A GitHub organization."""

    pending_cancellation_date: Optional[date] = None
    """The pending cancellation date for the seat, in `YYYY-MM-DD` format.

    This will be null unless the assignee's Copilot access has been canceled during
    the current billing cycle. If the seat has been cancelled, this corresponds to
    the start of the organization's next billing cycle.
    """

    plan_type: Optional[Literal["business", "enterprise", "unknown"]] = None
    """
    The Copilot plan of the organization, or the parent enterprise, when applicable.
    """

    updated_at: Optional[datetime] = None
    """**Closing down notice:** This field is no longer relevant and is closing down.

    Use the `created_at` field to determine when the assignee was last granted
    access to GitHub Copilot. Timestamp of when the assignee's GitHub Copilot access
    was last updated, in ISO 8601 format.
    """
