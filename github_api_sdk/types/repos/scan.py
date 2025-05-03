

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Scan"]


class Scan(BaseModel):
    completed_at: Optional[datetime] = None
    """The time that the scan was completed. Empty if the scan is running"""

    started_at: Optional[datetime] = None
    """The time that the scan was started. Empty if the scan is pending"""

    status: Optional[str] = None
    """The state of the scan. Either "completed", "running", or "pending" """

    type: Optional[str] = None
    """The type of scan"""
