

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..applications.user import User

__all__ = ["Milestone"]


class Milestone(BaseModel):
    id: int

    closed_at: Optional[datetime] = None

    closed_issues: int

    created_at: datetime

    creator: Optional[User] = None
    """A GitHub user."""

    description: Optional[str] = None

    due_on: Optional[datetime] = None

    html_url: str

    labels_url: str

    node_id: str

    number: int
    """The number of the milestone."""

    open_issues: int

    state: Literal["open", "closed"]
    """The state of the milestone."""

    title: str
    """The title of the milestone."""

    updated_at: datetime

    url: str
