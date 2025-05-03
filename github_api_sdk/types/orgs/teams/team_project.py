

from typing import Optional

from ...._models import BaseModel
from ..simple_user import SimpleUser

__all__ = ["TeamProject", "Permissions"]


class Permissions(BaseModel):
    admin: bool

    read: bool

    write: bool


class TeamProject(BaseModel):
    id: int

    body: Optional[str] = None

    columns_url: str

    created_at: str

    creator: SimpleUser
    """A GitHub user."""

    html_url: str

    name: str

    node_id: str

    number: int

    owner_url: str

    permissions: Permissions

    state: str

    updated_at: str

    url: str

    organization_permission: Optional[str] = None
    """The organization permission for this project.

    Only present when owner is an organization.
    """

    private: Optional[bool] = None
    """Whether the project is private or not.

    Only present when owner is an organization.
    """
