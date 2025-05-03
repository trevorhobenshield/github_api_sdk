

from typing import List, Optional

from ..._models import BaseModel
from .environment import Environment

__all__ = ["EnvironmentListResponse"]


class EnvironmentListResponse(BaseModel):
    environments: Optional[List[Environment]] = None

    total_count: Optional[int] = None
    """The number of environments in this repository"""
