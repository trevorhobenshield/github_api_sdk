

from typing import List

from ..._models import BaseModel

__all__ = ["Topic"]


class Topic(BaseModel):
    names: List[str]
