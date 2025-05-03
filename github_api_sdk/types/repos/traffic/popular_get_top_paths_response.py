

from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["PopularGetTopPathsResponse", "PopularGetTopPathsResponseItem"]


class PopularGetTopPathsResponseItem(BaseModel):
    count: int

    path: str

    title: str

    uniques: int


PopularGetTopPathsResponse: TypeAlias = List[PopularGetTopPathsResponseItem]
