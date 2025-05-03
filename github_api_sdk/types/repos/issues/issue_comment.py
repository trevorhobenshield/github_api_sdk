

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ...applications.user import User
from ..nullable_integration import NullableIntegration
from ...gists.author_association import AuthorAssociation
from ...orgs.teams.reaction_rollup import ReactionRollup

__all__ = ["IssueComment"]


class IssueComment(BaseModel):
    id: int
    """Unique identifier of the issue comment"""

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    created_at: datetime

    html_url: str

    issue_url: str

    node_id: str

    updated_at: datetime

    url: str
    """URL for the issue comment"""

    user: Optional[User] = None
    """A GitHub user."""

    body: Optional[str] = None
    """Contents of the issue comment"""

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    reactions: Optional[ReactionRollup] = None
