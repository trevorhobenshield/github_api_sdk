

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .orgs.simple_user import SimpleUser
from .applications.user import User

__all__ = ["RepoListStargazersResponse", "UnionMember1"]


class UnionMember1(BaseModel):
    starred_at: datetime

    user: Optional[User] = None
    """A GitHub user."""


RepoListStargazersResponse: TypeAlias = Union[List[SimpleUser], List[UnionMember1]]
