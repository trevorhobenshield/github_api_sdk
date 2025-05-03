

from typing import TYPE_CHECKING, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..enterprise import Enterprise
from ..orgs.simple_user import SimpleUser

__all__ = ["NullableIntegration", "Owner", "Permissions"]

Owner: TypeAlias = Union[SimpleUser, Enterprise]


class Permissions(BaseModel):
    checks: Optional[str] = None

    contents: Optional[str] = None

    deployments: Optional[str] = None

    issues: Optional[str] = None

    metadata: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...


class NullableIntegration(BaseModel):
    id: int
    """Unique identifier of the GitHub app"""

    created_at: datetime

    description: Optional[str] = None

    events: List[str]
    """The list of events for the GitHub app"""

    external_url: str

    html_url: str

    name: str
    """The name of the GitHub app"""

    node_id: str

    owner: Owner
    """A GitHub user."""

    permissions: Permissions
    """The set of permissions for the GitHub app"""

    updated_at: datetime

    client_id: Optional[str] = None

    client_secret: Optional[str] = None

    installations_count: Optional[int] = None
    """The number of installations associated with the GitHub app"""

    pem: Optional[str] = None

    slug: Optional[str] = None
    """The slug name of the GitHub app"""

    webhook_secret: Optional[str] = None
