

from typing import List

from ..._models import BaseModel
from .actions.actions_variable import ActionsVariable

__all__ = ["ActionListOrganizationVariablesResponse"]


class ActionListOrganizationVariablesResponse(BaseModel):
    total_count: int

    variables: List[ActionsVariable]
