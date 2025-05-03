

from typing import List
from typing_extensions import TypeAlias

from .users.gpg_key import GpgKey

__all__ = ["UserListGpgKeysResponse"]

UserListGpgKeysResponse: TypeAlias = List[GpgKey]
