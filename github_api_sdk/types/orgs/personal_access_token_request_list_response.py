

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .simple_user import SimpleUser

__all__ = [
    "PersonalAccessTokenRequestListResponse",
    "PersonalAccessTokenRequestListResponseItem",
    "PersonalAccessTokenRequestListResponseItemPermissions",
]


class PersonalAccessTokenRequestListResponseItemPermissions(BaseModel):
    organization: Optional[Dict[str, str]] = None

    other: Optional[Dict[str, str]] = None

    repository: Optional[Dict[str, str]] = None


class PersonalAccessTokenRequestListResponseItem(BaseModel):
    id: int
    """
    Unique identifier of the request for access via fine-grained personal access
    token. The `pat_request_id` used to review PAT requests.
    """

    created_at: str
    """Date and time when the request for access was created."""

    owner: SimpleUser
    """A GitHub user."""

    permissions: PersonalAccessTokenRequestListResponseItemPermissions
    """Permissions requested, categorized by type of permission."""

    reason: Optional[str] = None
    """Reason for requesting access."""

    repositories_url: str
    """
    URL to the list of repositories requested to be accessed via fine-grained
    personal access token. Should only be followed when `repository_selection` is
    `subset`.
    """

    repository_selection: Literal["none", "all", "subset"]
    """Type of repository selection requested."""

    token_expired: bool
    """Whether the associated fine-grained personal access token has expired."""

    token_expires_at: Optional[str] = None
    """Date and time when the associated fine-grained personal access token expires."""

    token_id: int
    """Unique identifier of the user's token.

    This field can also be found in audit log events and the organization's settings
    for their PAT grants.
    """

    token_last_used_at: Optional[str] = None
    """
    Date and time when the associated fine-grained personal access token was last
    used for authentication.
    """

    token_name: str
    """The name given to the user's token.

    This field can also be found in an organization's settings page for Active
    Tokens.
    """


PersonalAccessTokenRequestListResponse: TypeAlias = List[PersonalAccessTokenRequestListResponseItem]
