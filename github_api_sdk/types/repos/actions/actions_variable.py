

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ActionsVariable"]


class ActionsVariable(BaseModel):
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
