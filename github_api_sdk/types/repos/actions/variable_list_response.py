

from typing import List

from ...._models import BaseModel
from .actions_variable import ActionsVariable

__all__ = ["VariableListResponse"]


class VariableListResponse(BaseModel):
    total_count: int

    variables: List[ActionsVariable]
