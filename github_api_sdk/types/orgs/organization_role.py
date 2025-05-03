

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..applications.user import User

__all__ = ["OrganizationRole"]


class OrganizationRole(BaseModel):
    id: int
    """The unique identifier of the role."""

    created_at: datetime
    """The date and time the role was created."""

    name: str
    """The name of the role."""

    organization: Optional[User] = None
    """A GitHub user."""

    permissions: List[str]
    """A list of permissions included in this role."""

    updated_at: datetime
    """The date and time the role was last updated."""

    base_role: Optional[Literal["read", "triage", "write", "maintain", "admin"]] = None
    """The system role from which this role inherits permissions."""

    description: Optional[str] = None
    """A short description about who this role is for or what permissions it grants."""

    source: Optional[Literal["Organization", "Enterprise", "Predefined"]] = None
    """Source answers the question, "where did this role come from?" """
