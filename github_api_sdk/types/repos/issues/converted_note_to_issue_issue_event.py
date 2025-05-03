

from typing import Optional

from ...._models import BaseModel
from ...integration import Integration
from ...orgs.simple_user import SimpleUser

__all__ = ["ConvertedNoteToIssueIssueEvent", "ProjectCard"]


class ProjectCard(BaseModel):
    id: int

    column_name: str

    project_id: int

    project_url: str

    url: str

    previous_column_name: Optional[str] = None


class ConvertedNoteToIssueIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: str

    event: str

    node_id: str

    performed_via_github_app: Optional[Integration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    url: str

    project_card: Optional[ProjectCard] = None
