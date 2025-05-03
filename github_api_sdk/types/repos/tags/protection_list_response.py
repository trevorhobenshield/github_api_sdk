

from typing import List
from typing_extensions import TypeAlias

from .tag_protection import TagProtection

__all__ = ["ProtectionListResponse"]

ProtectionListResponse: TypeAlias = List[TagProtection]
