

from typing import List

from ..._models import BaseModel
from ..orgs.members.codespace import Codespace

__all__ = ["CodespaceListResponse"]


class CodespaceListResponse(BaseModel):
    codespaces: List[Codespace]

    total_count: int
