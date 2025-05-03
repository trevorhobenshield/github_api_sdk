

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..search_result_text_match import SearchResultTextMatch

__all__ = ["UserSearchResponse", "Item"]


class Item(BaseModel):
    id: int

    avatar_url: str

    events_url: str

    followers_url: str

    following_url: str

    gists_url: str

    gravatar_id: Optional[str] = None

    html_url: str

    login: str

    node_id: str

    organizations_url: str

    received_events_url: str

    repos_url: str

    score: float

    site_admin: bool

    starred_url: str

    subscriptions_url: str

    type: str

    url: str

    bio: Optional[str] = None

    blog: Optional[str] = None

    company: Optional[str] = None

    created_at: Optional[datetime] = None

    email: Optional[str] = None

    followers: Optional[int] = None

    following: Optional[int] = None

    hireable: Optional[bool] = None

    location: Optional[str] = None

    name: Optional[str] = None

    public_gists: Optional[int] = None

    public_repos: Optional[int] = None

    suspended_at: Optional[datetime] = None

    text_matches: Optional[List[SearchResultTextMatch]] = None

    updated_at: Optional[datetime] = None

    user_view_type: Optional[str] = None


class UserSearchResponse(BaseModel):
    incomplete_results: bool

    items: List[Item]

    total_count: int
