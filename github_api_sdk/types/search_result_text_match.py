

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchResultTextMatch", "Match"]


class Match(BaseModel):
    indices: Optional[List[int]] = None

    text: Optional[str] = None


class SearchResultTextMatch(BaseModel):
    fragment: Optional[str] = None

    matches: Optional[List[Match]] = None

    object_type: Optional[str] = None

    object_url: Optional[str] = None

    property: Optional[str] = None
