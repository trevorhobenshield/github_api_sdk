

from typing import List
from typing_extensions import TypeAlias

from .....orgs.simple_user import SimpleUser

__all__ = ["UserSetResponse"]

UserSetResponse: TypeAlias = List[SimpleUser]
