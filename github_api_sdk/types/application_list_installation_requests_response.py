

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .enterprise import Enterprise
from .orgs.simple_user import SimpleUser

__all__ = [
    "ApplicationListInstallationRequestsResponse",
    "ApplicationListInstallationRequestsResponseItem",
    "ApplicationListInstallationRequestsResponseItemAccount",
]

ApplicationListInstallationRequestsResponseItemAccount: TypeAlias = Union[SimpleUser, Enterprise]


class ApplicationListInstallationRequestsResponseItem(BaseModel):
    id: int
    """Unique identifier of the request installation."""

    account: ApplicationListInstallationRequestsResponseItemAccount
    """A GitHub user."""

    created_at: datetime

    requester: SimpleUser
    """A GitHub user."""

    node_id: Optional[str] = None


ApplicationListInstallationRequestsResponse: TypeAlias = List[ApplicationListInstallationRequestsResponseItem]
