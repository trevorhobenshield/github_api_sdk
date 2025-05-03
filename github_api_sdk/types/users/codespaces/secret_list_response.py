

from typing import List

from ...._models import BaseModel
from .codespace_secret import CodespaceSecret

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    secrets: List[CodespaceSecret]

    total_count: int
