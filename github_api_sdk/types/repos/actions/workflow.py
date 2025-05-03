

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Workflow"]


class Workflow(BaseModel):
    id: int

    badge_url: str

    created_at: datetime

    html_url: str

    name: str

    node_id: str

    path: str

    state: Literal["active", "deleted", "disabled_fork", "disabled_inactivity", "disabled_manually"]

    updated_at: datetime

    url: str

    deleted_at: Optional[datetime] = None
