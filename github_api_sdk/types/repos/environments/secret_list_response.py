

from typing import List

from ...._models import BaseModel
from ..actions.actions_secret import ActionsSecret

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    secrets: List[ActionsSecret]

    total_count: int
