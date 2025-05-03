

from typing import Optional

from ...._models import BaseModel
from ...orgs.simple_user import SimpleUser
from ..nullable_integration import NullableIntegration

__all__ = ["ReviewDismissedIssueEvent", "DismissedReview"]


class DismissedReview(BaseModel):
    dismissal_message: Optional[str] = None

    review_id: int

    state: str

    dismissal_commit_id: Optional[str] = None


class ReviewDismissedIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: str

    dismissed_review: DismissedReview

    event: str

    node_id: str

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    url: str
