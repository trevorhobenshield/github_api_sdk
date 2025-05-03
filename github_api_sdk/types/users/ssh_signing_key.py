

from datetime import datetime

from ..._models import BaseModel

__all__ = ["SSHSigningKey"]


class SSHSigningKey(BaseModel):
    id: int

    created_at: datetime

    key: str

    title: str
