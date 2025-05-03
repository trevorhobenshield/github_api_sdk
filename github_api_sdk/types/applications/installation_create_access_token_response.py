

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .permissions import Permissions
from ..users.repository import Repository

__all__ = ["InstallationCreateAccessTokenResponse"]


class InstallationCreateAccessTokenResponse(BaseModel):
    token: str

    expires_at: str

    has_multiple_single_files: Optional[bool] = None

    permissions: Optional[Permissions] = None
    """The permissions granted to the user access token."""

    repositories: Optional[List[Repository]] = None

    repository_selection: Optional[Literal["all", "selected"]] = None

    single_file: Optional[str] = None

    single_file_paths: Optional[List[str]] = None
