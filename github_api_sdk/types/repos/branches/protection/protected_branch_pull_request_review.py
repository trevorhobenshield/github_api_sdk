

from typing import List, Optional

from ....._models import BaseModel
from ....orgs.team import Team
from ....integration import Integration
from ....orgs.simple_user import SimpleUser

__all__ = ["ProtectedBranchPullRequestReview", "BypassPullRequestAllowances", "DismissalRestrictions"]


class BypassPullRequestAllowances(BaseModel):
    apps: Optional[List[Optional[Integration]]] = None
    """The list of apps allowed to bypass pull request requirements."""

    teams: Optional[List[Team]] = None
    """The list of teams allowed to bypass pull request requirements."""

    users: Optional[List[SimpleUser]] = None
    """The list of users allowed to bypass pull request requirements."""


class DismissalRestrictions(BaseModel):
    apps: Optional[List[Optional[Integration]]] = None
    """The list of apps with review dismissal access."""

    teams: Optional[List[Team]] = None
    """The list of teams with review dismissal access."""

    teams_url: Optional[str] = None

    url: Optional[str] = None

    users: Optional[List[SimpleUser]] = None
    """The list of users with review dismissal access."""

    users_url: Optional[str] = None


class ProtectedBranchPullRequestReview(BaseModel):
    dismiss_stale_reviews: bool

    require_code_owner_reviews: bool

    bypass_pull_request_allowances: Optional[BypassPullRequestAllowances] = None
    """Allow specific users, teams, or apps to bypass pull request requirements."""

    dismissal_restrictions: Optional[DismissalRestrictions] = None

    require_last_push_approval: Optional[bool] = None
    """
    Whether the most recent push must be approved by someone other than the person
    who pushed it.
    """

    required_approving_review_count: Optional[int] = None

    url: Optional[str] = None
