

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .simple_user import SimpleUser

__all__ = [
    "PersonalAccessTokenListResponse",
    "PersonalAccessTokenListResponseItem",
    "PersonalAccessTokenListResponseItemPermissions",
]


class PersonalAccessTokenListResponseItemPermissions(BaseModel):
    organization: Optional[Dict[str, str]] = None

    other: Optional[Dict[str, str]] = None

    repository: Optional[Dict[str, str]] = None


class PersonalAccessTokenListResponseItem(BaseModel):
    id: int
    """Unique identifier of the fine-grained personal access token grant.

    The `pat_id` used to get details about an approved fine-grained personal access
    token.
    """

    access_granted_at: str
    """
    Date and time when the fine-grained personal access token was approved to access
    the organization.
    """

    owner: SimpleUser
    """A GitHub user."""

    permissions: PersonalAccessTokenListResponseItemPermissions
    """Permissions requested, categorized by type of permission."""

    repositories_url: str
    """
    URL to the list of repositories the fine-grained personal access token can
    access. Only follow when `repository_selection` is `subset`.
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


PersonalAccessTokenListResponse: TypeAlias = List[PersonalAccessTokenListResponseItem]
