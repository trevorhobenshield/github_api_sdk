

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["UserListPublicKeysResponse", "UserListPublicKeysResponseItem"]


class UserListPublicKeysResponseItem(BaseModel):
    id: int

    key: str


UserListPublicKeysResponse: TypeAlias = List[UserListPublicKeysResponseItem]
