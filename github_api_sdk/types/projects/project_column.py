

from datetime import datetime

from ..._models import BaseModel

__all__ = ["ProjectColumn"]


class ProjectColumn(BaseModel):
    id: int
    """The unique identifier of the project column"""

    cards_url: str

    created_at: datetime

    name: str
    """Name of the project column"""

    node_id: str

    project_url: str

    updated_at: datetime

    url: str
