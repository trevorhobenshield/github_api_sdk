

from typing import List

from .codespace import Codespace
from ...._models import BaseModel

__all__ = ["CodespaceListResponse"]


class CodespaceListResponse(BaseModel):
    codespaces: List[Codespace]

    total_count: int
