

from typing import List

from ..._models import BaseModel
from .traffic.traffic import Traffic

__all__ = ["TrafficGetViewsResponse"]


class TrafficGetViewsResponse(BaseModel):
    count: int

    uniques: int

    views: List[Traffic]
