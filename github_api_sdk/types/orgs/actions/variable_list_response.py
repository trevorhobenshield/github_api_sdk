

from typing import List

from ...._models import BaseModel
from .organization_variable import OrganizationVariable

__all__ = ["VariableListResponse"]


class VariableListResponse(BaseModel):
    total_count: int

    variables: List[OrganizationVariable]
