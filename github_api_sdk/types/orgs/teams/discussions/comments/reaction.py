

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel
from .....applications.user import User

__all__ = ["Reaction"]


class Reaction(BaseModel):
    id: int

    content: Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"]
    """The reaction to use"""

    created_at: datetime

    node_id: str

    user: Optional[User] = None
    """A GitHub user."""
