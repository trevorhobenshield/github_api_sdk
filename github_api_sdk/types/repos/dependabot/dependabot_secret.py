

from datetime import datetime

from ...._models import BaseModel

__all__ = ["DependabotSecret"]


class DependabotSecret(BaseModel):
    created_at: datetime

    name: str
    """The name of the secret."""

    updated_at: datetime
