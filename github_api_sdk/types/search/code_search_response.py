

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..minimal_repository import MinimalRepository
from ..search_result_text_match import SearchResultTextMatch

__all__ = ["CodeSearchResponse", "Item"]


class Item(BaseModel):
    git_url: str

    html_url: str

    name: str

    path: str

    repository: MinimalRepository
    """Minimal Repository"""

    score: float

    sha: str

    url: str

    file_size: Optional[int] = None

    language: Optional[str] = None

    last_modified_at: Optional[datetime] = None

    line_numbers: Optional[List[str]] = None

    text_matches: Optional[List[SearchResultTextMatch]] = None


class CodeSearchResponse(BaseModel):
    incomplete_results: bool

    items: List[Item]

    total_count: int
