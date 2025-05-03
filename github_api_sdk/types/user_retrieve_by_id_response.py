

from typing import Union
from typing_extensions import TypeAlias

from .public_user import PublicUser
from .private_user import PrivateUser

__all__ = ["UserRetrieveByIDResponse"]

UserRetrieveByIDResponse: TypeAlias = Union[PrivateUser, PublicUser]
