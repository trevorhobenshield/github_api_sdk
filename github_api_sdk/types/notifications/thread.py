

from typing import Optional

from ..._models import BaseModel
from ..minimal_repository import MinimalRepository

__all__ = ["Thread", "Subject"]


class Subject(BaseModel):
    latest_comment_url: str

    title: str

    type: str

    url: str


class Thread(BaseModel):
    id: str

    last_read_at: Optional[str] = None

    reason: str

    repository: MinimalRepository
    """Minimal Repository"""

    subject: Subject

    subscription_url: str

    unread: bool

    updated_at: str

    url: str
