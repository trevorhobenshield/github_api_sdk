

from typing import List
from typing_extensions import TypeAlias

from .key import Key

__all__ = ["KeyListResponse"]

KeyListResponse: TypeAlias = List[Key]
