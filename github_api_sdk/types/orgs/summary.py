

from typing import List, Optional
from datetime import datetime

from .team import Team
from .state import State
from ..._models import BaseModel
from .simple_user import SimpleUser

__all__ = ["Summary", "AlertStats"]


class AlertStats(BaseModel):
    closed_count: int
    """The number of closed alerts"""

    in_progress_count: int
    """The number of in-progress alerts"""

    open_count: int
    """The number of open alerts"""


class Summary(BaseModel):
    contact_link: Optional[str] = None
    """The contact link of the campaign."""

    created_at: datetime
    """
    The date and time the campaign was created, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    description: str
    """The campaign description"""

    ends_at: datetime
    """
    The date and time the campaign has ended, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    managers: List[SimpleUser]
    """The campaign managers"""

    number: int
    """The number of the newly created campaign"""

    state: State
    """Indicates whether a campaign is open or closed"""

    updated_at: datetime
    """
    The date and time the campaign was last updated, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    alert_stats: Optional[AlertStats] = None

    closed_at: Optional[datetime] = None
    """
    The date and time the campaign was closed, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ. Will be null if the campaign is still open.
    """

    name: Optional[str] = None
    """The campaign name"""

    published_at: Optional[datetime] = None
    """
    The date and time the campaign was published, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    team_managers: Optional[List[Team]] = None
    """The campaign team managers"""
