

from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["PopularGetTopReferrersResponse", "PopularGetTopReferrersResponseItem"]


class PopularGetTopReferrersResponseItem(BaseModel):
    count: int

    referrer: str

    uniques: int


PopularGetTopReferrersResponse: TypeAlias = List[PopularGetTopReferrersResponseItem]
