

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["StatGetCommitActivityResponse", "StatGetCommitActivityResponseItem"]


class StatGetCommitActivityResponseItem(BaseModel):
    days: List[int]

    total: int

    week: int


StatGetCommitActivityResponse: TypeAlias = List[StatGetCommitActivityResponseItem]
