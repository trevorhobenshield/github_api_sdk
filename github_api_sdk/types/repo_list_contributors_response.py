

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["RepoListContributorsResponse", "RepoListContributorsResponseItem"]


class RepoListContributorsResponseItem(BaseModel):
    contributions: int

    type: str

    id: Optional[int] = None

    avatar_url: Optional[str] = None

    email: Optional[str] = None

    events_url: Optional[str] = None

    followers_url: Optional[str] = None

    following_url: Optional[str] = None

    gists_url: Optional[str] = None

    gravatar_id: Optional[str] = None

    html_url: Optional[str] = None

    login: Optional[str] = None

    name: Optional[str] = None

    node_id: Optional[str] = None

    organizations_url: Optional[str] = None

    received_events_url: Optional[str] = None

    repos_url: Optional[str] = None

    site_admin: Optional[bool] = None

    starred_url: Optional[str] = None

    subscriptions_url: Optional[str] = None

    url: Optional[str] = None

    user_view_type: Optional[str] = None


RepoListContributorsResponse: TypeAlias = List[RepoListContributorsResponseItem]
