

from typing import Optional

from ...._models import BaseModel
from ...orgs.team import Team
from ...orgs.simple_user import SimpleUser
from ..nullable_integration import NullableIntegration

__all__ = ["ReviewRequestedIssueEvent"]


class ReviewRequestedIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: str

    event: str

    node_id: str

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    review_requester: SimpleUser
    """A GitHub user."""

    url: str

    requested_reviewer: Optional[SimpleUser] = None
    """A GitHub user."""

    requested_team: Optional[Team] = None
    """
    Groups of organization members that gives permissions on specified repositories.
    """
