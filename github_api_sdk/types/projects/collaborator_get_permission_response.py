

from typing import Optional

from ..._models import BaseModel
from ..applications.user import User

__all__ = ["CollaboratorGetPermissionResponse"]


class CollaboratorGetPermissionResponse(BaseModel):
    permission: str

    user: Optional[User] = None
    """A GitHub user."""
