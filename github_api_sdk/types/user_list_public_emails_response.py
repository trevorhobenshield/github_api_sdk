

from typing import List
from typing_extensions import TypeAlias

from .users.email import Email

__all__ = ["UserListPublicEmailsResponse"]

UserListPublicEmailsResponse: TypeAlias = List[Email]
