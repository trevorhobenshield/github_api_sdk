

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..users.repository import Repository
from ..applications.user import User

__all__ = ["Migration"]


class Migration(BaseModel):
    id: int

    created_at: datetime

    exclude_attachments: bool

    exclude_git_data: bool

    exclude_metadata: bool

    exclude_owner_projects: bool

    exclude_releases: bool

    guid: str

    lock_repositories: bool

    node_id: str

    org_metadata_only: bool

    owner: Optional[User] = None
    """A GitHub user."""

    repositories: List[Repository]
    """The repositories included in the migration.

    Only returned for export migrations.
    """

    state: str

    updated_at: datetime

    url: str

    archive_url: Optional[str] = None

    exclude: Optional[List[str]] = None
    """
    Exclude related items from being returned in the response in order to improve
    performance of the request. The array can include any of: `"repositories"`.
    """
