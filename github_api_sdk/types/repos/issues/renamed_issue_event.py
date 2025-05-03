

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...orgs.simple_user import SimpleUser
from ..nullable_integration import NullableIntegration

__all__ = ["RenamedIssueEvent", "Rename"]


class Rename(BaseModel):
    from_: str = FieldInfo(alias="from")

    to: str


class RenamedIssueEvent(BaseModel):
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

    rename: Rename

    url: str
