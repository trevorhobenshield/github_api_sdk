

from typing import Optional

from ..._models import BaseModel
from ..orgs.simple_user import SimpleUser

__all__ = ["CodespaceGetDefaultAttributesResponse", "Defaults"]


class Defaults(BaseModel):
    devcontainer_path: Optional[str] = None

    location: str


class CodespaceGetDefaultAttributesResponse(BaseModel):
    billable_owner: Optional[SimpleUser] = None
    """A GitHub user."""

    defaults: Optional[Defaults] = None
