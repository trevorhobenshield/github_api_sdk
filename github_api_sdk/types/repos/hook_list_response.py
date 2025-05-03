

from typing import List
from typing_extensions import TypeAlias

from .hook import Hook

__all__ = ["HookListResponse"]

HookListResponse: TypeAlias = List[Hook]
