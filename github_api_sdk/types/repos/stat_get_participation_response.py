

from typing import List

from ..._models import BaseModel

__all__ = ["StatGetParticipationResponse"]


class StatGetParticipationResponse(BaseModel):
    all: List[int]

    owner: List[int]
