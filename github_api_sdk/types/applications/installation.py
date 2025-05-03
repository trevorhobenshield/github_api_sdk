

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .user import User
from ..._models import BaseModel
from ..enterprise import Enterprise
from .permissions import Permissions
from ..orgs.simple_user import SimpleUser

__all__ = ["Installation", "Account"]

Account: TypeAlias = Union[SimpleUser, Enterprise, None]


class Installation(BaseModel):
    id: int
    """The ID of the installation."""

    access_tokens_url: str

    account: Optional[Account] = None
    """A GitHub user."""

    app_id: int

    app_slug: str

    created_at: datetime

    events: List[str]

    html_url: str

    permissions: Permissions
    """The permissions granted to the user access token."""

    repositories_url: str

    repository_selection: Literal["all", "selected"]
    """
    Describe whether all repositories have been selected or there's a selection
    involved
    """

    single_file_name: Optional[str] = None

    suspended_at: Optional[datetime] = None

    suspended_by: Optional[User] = None
    """A GitHub user."""

    target_id: int
    """The ID of the user or organization this token is being scoped to."""

    target_type: str

    updated_at: datetime

    contact_email: Optional[str] = None

    has_multiple_single_files: Optional[bool] = None

    single_file_paths: Optional[List[str]] = None
