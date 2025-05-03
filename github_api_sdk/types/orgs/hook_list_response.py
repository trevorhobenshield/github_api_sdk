

from typing import List
from typing_extensions import TypeAlias

from .org_hook import OrgHook

__all__ = ["HookListResponse"]

HookListResponse: TypeAlias = List[OrgHook]
