

from typing import List
from typing_extensions import TypeAlias

from .gpg_key import GpgKey

__all__ = ["GpgKeyListResponse"]

GpgKeyListResponse: TypeAlias = List[GpgKey]
