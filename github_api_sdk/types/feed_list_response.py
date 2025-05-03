

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .link_with_type import LinkWithType

__all__ = ["FeedListResponse", "_Links"]


class _Links(BaseModel):
    timeline: LinkWithType
    """Hypermedia Link with Type"""

    user: LinkWithType
    """Hypermedia Link with Type"""

    current_user: Optional[LinkWithType] = None
    """Hypermedia Link with Type"""

    current_user_actor: Optional[LinkWithType] = None
    """Hypermedia Link with Type"""

    current_user_organization: Optional[LinkWithType] = None
    """Hypermedia Link with Type"""

    current_user_organizations: Optional[List[LinkWithType]] = None

    current_user_public: Optional[LinkWithType] = None
    """Hypermedia Link with Type"""

    repository_discussions: Optional[LinkWithType] = None
    """Hypermedia Link with Type"""

    repository_discussions_category: Optional[LinkWithType] = None
    """Hypermedia Link with Type"""

    security_advisories: Optional[LinkWithType] = None
    """Hypermedia Link with Type"""


class FeedListResponse(BaseModel):
    api_links: _Links = FieldInfo(alias="_links")

    timeline_url: str

    user_url: str

    current_user_actor_url: Optional[str] = None

    current_user_organization_url: Optional[str] = None

    current_user_organization_urls: Optional[List[str]] = None

    current_user_public_url: Optional[str] = None

    current_user_url: Optional[str] = None

    repository_discussions_category_url: Optional[str] = None
    """A feed of discussions for a given repository and category."""

    repository_discussions_url: Optional[str] = None
    """A feed of discussions for a given repository."""

    security_advisories_url: Optional[str] = None
