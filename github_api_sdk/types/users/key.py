

from datetime import datetime

from ..._models import BaseModel

__all__ = ["Key"]


class Key(BaseModel):
    id: int

    created_at: datetime

    key: str

    read_only: bool

    title: str

    url: str

    verified: bool
