

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..orgs.simple_user import SimpleUser
from .releases.release_asset import ReleaseAsset
from ..orgs.teams.reaction_rollup import ReactionRollup

__all__ = ["Release"]


class Release(BaseModel):
    id: int

    assets: List[ReleaseAsset]

    assets_url: str

    author: SimpleUser
    """A GitHub user."""

    created_at: datetime

    draft: bool
    """true to create a draft (unpublished) release, false to create a published one."""

    html_url: str

    name: Optional[str] = None

    node_id: str

    prerelease: bool
    """Whether to identify the release as a prerelease or a full release."""

    published_at: Optional[datetime] = None

    tag_name: str
    """The name of the tag."""

    tarball_url: Optional[str] = None

    target_commitish: str
    """
    Specifies the commitish value that determines where the Git tag is created from.
    """

    upload_url: str

    url: str

    zipball_url: Optional[str] = None

    body: Optional[str] = None

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    discussion_url: Optional[str] = None
    """The URL of the release discussion."""

    mentions_count: Optional[int] = None

    reactions: Optional[ReactionRollup] = None
