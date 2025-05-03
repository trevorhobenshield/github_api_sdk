

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CodespaceExportDetails"]


class CodespaceExportDetails(BaseModel):
    id: Optional[str] = None
    """Id for the export details"""

    branch: Optional[str] = None
    """Name of the exported branch"""

    completed_at: Optional[datetime] = None
    """Completion time of the last export operation"""

    export_url: Optional[str] = None
    """Url for fetching export details"""

    html_url: Optional[str] = None
    """Web url for the exported branch"""

    sha: Optional[str] = None
    """Git commit SHA of the exported branch"""

    state: Optional[str] = None
    """State of the latest export"""
