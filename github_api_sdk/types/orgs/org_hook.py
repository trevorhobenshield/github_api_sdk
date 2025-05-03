

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["OrgHook", "Config"]


class Config(BaseModel):
    content_type: Optional[str] = None

    insecure_ssl: Optional[str] = None

    secret: Optional[str] = None

    url: Optional[str] = None


class OrgHook(BaseModel):
    id: int

    active: bool

    config: Config

    created_at: datetime

    events: List[str]

    name: str

    ping_url: str

    type: str

    updated_at: datetime

    url: str

    deliveries_url: Optional[str] = None
