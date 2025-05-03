

from typing import List, Optional

from ..._models import BaseModel
from .organization_role import OrganizationRole

__all__ = ["OrganizationRoleListResponse"]


class OrganizationRoleListResponse(BaseModel):
    roles: Optional[List[OrganizationRole]] = None
    """The list of organization roles available to the organization."""

    total_count: Optional[int] = None
    """The total number of organization roles available to the organization."""
