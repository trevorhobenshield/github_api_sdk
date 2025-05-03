

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..search_result_text_match import SearchResultTextMatch

__all__ = [
    "TopicSearchResponse",
    "Item",
    "ItemAlias",
    "ItemAliasTopicRelation",
    "ItemRelated",
    "ItemRelatedTopicRelation",
]


class ItemAliasTopicRelation(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    relation_type: Optional[str] = None

    topic_id: Optional[int] = None


class ItemAlias(BaseModel):
    topic_relation: Optional[ItemAliasTopicRelation] = None


class ItemRelatedTopicRelation(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    relation_type: Optional[str] = None

    topic_id: Optional[int] = None


class ItemRelated(BaseModel):
    topic_relation: Optional[ItemRelatedTopicRelation] = None


class Item(BaseModel):
    created_at: datetime

    created_by: Optional[str] = None

    curated: bool

    description: Optional[str] = None

    display_name: Optional[str] = None

    featured: bool

    name: str

    released: Optional[str] = None

    score: float

    short_description: Optional[str] = None

    updated_at: datetime

    aliases: Optional[List[ItemAlias]] = None

    logo_url: Optional[str] = None

    related: Optional[List[ItemRelated]] = None

    repository_count: Optional[int] = None

    text_matches: Optional[List[SearchResultTextMatch]] = None


class TopicSearchResponse(BaseModel):
    incomplete_results: bool

    items: List[Item]

    total_count: int
