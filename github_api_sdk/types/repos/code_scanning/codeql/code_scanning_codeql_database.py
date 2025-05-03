

from typing import Optional
from datetime import datetime

from ....._models import BaseModel
from ....orgs.simple_user import SimpleUser

__all__ = ["CodeScanningCodeqlDatabase"]


class CodeScanningCodeqlDatabase(BaseModel):
    id: int
    """The ID of the CodeQL database."""

    content_type: str
    """The MIME type of the CodeQL database file."""

    created_at: datetime
    """
    The date and time at which the CodeQL database was created, in ISO 8601
    format':' YYYY-MM-DDTHH:MM:SSZ.
    """

    language: str
    """The language of the CodeQL database."""

    name: str
    """The name of the CodeQL database."""

    size: int
    """The size of the CodeQL database file in bytes."""

    updated_at: datetime
    """
    The date and time at which the CodeQL database was last updated, in ISO 8601
    format':' YYYY-MM-DDTHH:MM:SSZ.
    """

    uploader: SimpleUser
    """A GitHub user."""

    url: str
    """The URL at which to download the CodeQL database.

    The `Accept` header must be set to the value of the `content_type` property.
    """

    commit_oid: Optional[str] = None
    """The commit SHA of the repository at the time the CodeQL database was created."""
