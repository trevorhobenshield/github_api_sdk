

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..organization import Organization
from ..applications.user import User

__all__ = ["OrgMembership", "Permissions"]


class Permissions(BaseModel):
    can_create_repository: bool


class OrgMembership(BaseModel):
    organization: Organization
    """A GitHub organization."""

    organization_url: str

    role: Literal["admin", "member", "billing_manager"]
    """The user's membership type in the organization."""

    state: Literal["active", "pending"]
    """The state of the member in the organization.

    The `pending` state indicates the user has not yet accepted an invitation.
    """

    url: str

    user: Optional[User] = None
    """A GitHub user."""

    permissions: Optional[Permissions] = None
