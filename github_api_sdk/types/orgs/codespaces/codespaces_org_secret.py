

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CodespacesOrgSecret"]


class CodespacesOrgSecret(BaseModel):
    created_at: datetime
    """
    The date and time at which the secret was created, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    name: str
    """The name of the secret"""

    updated_at: datetime
    """
    The date and time at which the secret was created, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    visibility: Literal["all", "private", "selected"]
    """The type of repositories in the organization that the secret is visible to"""

    selected_repositories_url: Optional[str] = None
    """
    The API URL at which the list of repositories this secret is visible to can be
    retrieved
    """
