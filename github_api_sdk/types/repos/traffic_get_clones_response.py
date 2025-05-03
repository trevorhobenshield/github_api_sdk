

from typing import List

from ..._models import BaseModel
from .traffic.traffic import Traffic

__all__ = ["TrafficGetClonesResponse"]


class TrafficGetClonesResponse(BaseModel):
    clones: List[Traffic]

    count: int

    uniques: int
