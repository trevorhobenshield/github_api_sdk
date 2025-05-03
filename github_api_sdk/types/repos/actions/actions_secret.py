

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ActionsSecret"]


class ActionsSecret(BaseModel):
    created_at: datetime

    name: str
    """The name of the secret."""

    updated_at: datetime
