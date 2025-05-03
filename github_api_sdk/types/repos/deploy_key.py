

from typing import Optional

from ..._models import BaseModel

__all__ = ["DeployKey"]


class DeployKey(BaseModel):
    id: int

    created_at: str

    key: str

    read_only: bool

    title: str

    url: str

    verified: bool

    added_by: Optional[str] = None

    enabled: Optional[bool] = None

    last_used: Optional[str] = None
