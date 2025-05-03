

from datetime import datetime

from ...._models import BaseModel

__all__ = ["RepoCodespacesSecret"]


class RepoCodespacesSecret(BaseModel):
    created_at: datetime

    name: str
    """The name of the secret."""

    updated_at: datetime
