

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Artifact", "WorkflowRun"]


class WorkflowRun(BaseModel):
    id: Optional[int] = None

    head_branch: Optional[str] = None

    head_repository_id: Optional[int] = None

    head_sha: Optional[str] = None

    repository_id: Optional[int] = None


class Artifact(BaseModel):
    id: int

    archive_download_url: str

    created_at: Optional[datetime] = None

    expired: bool
    """Whether or not the artifact has expired."""

    expires_at: Optional[datetime] = None

    name: str
    """The name of the artifact."""

    node_id: str

    size_in_bytes: int
    """The size in bytes of the artifact."""

    updated_at: Optional[datetime] = None

    url: str

    digest: Optional[str] = None
    """The SHA256 digest of the artifact.

    This field will only be populated on artifacts uploaded with upload-artifact v4
    or newer. For older versions, this field will be null.
    """

    workflow_run: Optional[WorkflowRun] = None
