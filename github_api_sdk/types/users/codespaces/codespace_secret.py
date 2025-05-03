

from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CodespaceSecret"]


class CodespaceSecret(BaseModel):
    created_at: datetime
    """
    The date and time at which the secret was created, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    name: str
    """The name of the secret"""

    selected_repositories_url: str
    """
    The API URL at which the list of repositories this secret is visible to can be
    retrieved
    """

    updated_at: datetime
    """
    The date and time at which the secret was last updated, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    visibility: Literal["all", "private", "selected"]
    """The type of repositories in the organization that the secret is visible to"""
