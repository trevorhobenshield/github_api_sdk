

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..applications.user import User

__all__ = ["Project"]


class Project(BaseModel):
    id: int

    body: Optional[str] = None
    """Body of the project"""

    columns_url: str

    created_at: datetime

    creator: Optional[User] = None
    """A GitHub user."""

    html_url: str

    name: str
    """Name of the project"""

    node_id: str

    number: int

    owner_url: str

    state: str
    """State of the project; either 'open' or 'closed'"""

    updated_at: datetime

    url: str

    organization_permission: Optional[Literal["read", "write", "admin", "none"]] = None
    """The baseline permission that all organization members have on this project.

    Only present if owner is an organization.
    """

    private: Optional[bool] = None
    """Whether or not this project can be seen by everyone.

    Only present if owner is an organization.
    """
