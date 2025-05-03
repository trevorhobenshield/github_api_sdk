

from typing import Optional

from ...._models import BaseModel
from ...orgs.simple_user import SimpleUser
from ..nullable_integration import NullableIntegration

__all__ = ["LabeledIssueEvent", "Label"]


class Label(BaseModel):
    color: str

    name: str


class LabeledIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: str

    event: str

    label: Label

    node_id: str

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    url: str
