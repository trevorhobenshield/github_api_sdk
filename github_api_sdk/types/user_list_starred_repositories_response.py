

from typing import List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .users.repository import Repository

__all__ = ["UserListStarredRepositoriesResponse", "UnionMember0"]


class UnionMember0(BaseModel):
    repo: Repository
    """A repository on GitHub."""

    starred_at: datetime


UserListStarredRepositoriesResponse: TypeAlias = Union[List[UnionMember0], List[Repository]]
