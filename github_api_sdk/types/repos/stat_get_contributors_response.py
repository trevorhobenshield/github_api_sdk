

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..applications.user import User

__all__ = ["StatGetContributorsResponse", "StatGetContributorsResponseItem", "StatGetContributorsResponseItemWeek"]


class StatGetContributorsResponseItemWeek(BaseModel):
    a: Optional[int] = None

    c: Optional[int] = None

    d: Optional[int] = None

    w: Optional[int] = None


class StatGetContributorsResponseItem(BaseModel):
    author: Optional[User] = None
    """A GitHub user."""

    total: int

    weeks: List[StatGetContributorsResponseItemWeek]


StatGetContributorsResponse: TypeAlias = List[StatGetContributorsResponseItem]
