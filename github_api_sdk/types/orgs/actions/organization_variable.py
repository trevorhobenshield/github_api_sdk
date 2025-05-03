

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OrganizationVariable"]


class OrganizationVariable(BaseModel):
    created_at: datetime
    """
    The date and time at which the variable was created, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    name: str
    """The name of the variable."""

    updated_at: datetime
    """
    The date and time at which the variable was last updated, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    value: str
    """The value of the variable."""

    visibility: Literal["all", "private", "selected"]
    """Visibility of a variable"""

    selected_repositories_url: Optional[str] = None
