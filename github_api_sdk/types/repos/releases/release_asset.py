

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...applications.user import User

__all__ = ["ReleaseAsset"]


class ReleaseAsset(BaseModel):
    id: int

    browser_download_url: str

    content_type: str

    created_at: datetime

    download_count: int

    label: Optional[str] = None

    name: str
    """The file name of the asset."""

    node_id: str

    size: int

    state: Literal["uploaded", "open"]
    """State of the release asset."""

    updated_at: datetime

    uploader: Optional[User] = None
    """A GitHub user."""

    url: str
