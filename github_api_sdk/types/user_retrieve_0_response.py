

from typing import Union
from typing_extensions import TypeAlias

from .public_user import PublicUser
from .private_user import PrivateUser

__all__ = ["UserRetrieve0Response"]

UserRetrieve0Response: TypeAlias = Union[PrivateUser, PublicUser]
