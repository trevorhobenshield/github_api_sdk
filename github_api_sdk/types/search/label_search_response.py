

from typing import List, Optional

from ..._models import BaseModel
from ..search_result_text_match import SearchResultTextMatch

__all__ = ["LabelSearchResponse", "Item"]


class Item(BaseModel):
    id: int

    color: str

    default: bool

    description: Optional[str] = None

    name: str

    node_id: str

    score: float

    url: str

    text_matches: Optional[List[SearchResultTextMatch]] = None


class LabelSearchResponse(BaseModel):
    incomplete_results: bool

    items: List[Item]

    total_count: int
