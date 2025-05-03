

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...users.repository import Repository

__all__ = ["AuthenticationToken"]


class AuthenticationToken(BaseModel):
    token: str
    """The token used for authentication"""

    expires_at: datetime
    """The time this token expires"""

    permissions: Optional[object] = None

    repositories: Optional[List[Repository]] = None
    """The repositories this token has access to"""

    repository_selection: Optional[Literal["all", "selected"]] = None
    """
    Describe whether all repositories have been selected or there's a selection
    involved
    """

    single_file: Optional[str] = None
