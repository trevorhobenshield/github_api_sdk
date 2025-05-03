

from typing import List

from ..._models import BaseModel
from ..repos.codespace_machine import CodespaceMachine

__all__ = ["CodespaceListMachinesResponse"]


class CodespaceListMachinesResponse(BaseModel):
    machines: List[CodespaceMachine]

    total_count: int
