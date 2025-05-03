

from typing import List

from ..._models import BaseModel
from .members.codespace import Codespace

__all__ = ["CodespaceListResponse"]


class CodespaceListResponse(BaseModel):
    codespaces: List[Codespace]

    total_count: int
