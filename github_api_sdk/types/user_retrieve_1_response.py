

from typing import Union
from typing_extensions import TypeAlias

from .public_user import PublicUser
from .private_user import PrivateUser

__all__ = ["UserRetrieve1Response"]

UserRetrieve1Response: TypeAlias = Union[PrivateUser, PublicUser]
