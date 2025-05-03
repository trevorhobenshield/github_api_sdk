

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .state import State
from ..._utils import PropertyInfo

__all__ = ["CampaignUpdateParams"]


class CampaignUpdateParams(TypedDict, total=False):
    org: Required[str]

    contact_link: str | None
    """The contact link of the campaign. Must be a URI."""

    description: str
    """A description for the campaign"""

    ends_at: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """
    The end date and time of the campaign, in ISO 8601 format':'
    YYYY-MM-DDTHH:MM:SSZ.
    """

    managers: list[str]
    """The logins of the users to set as the campaign managers.

    At this time, only a single manager can be supplied.
    """

    name: str
    """The name of the campaign"""

    state: State
    """Indicates whether a campaign is open or closed"""

    team_managers: list[str]
    """The slugs of the teams to set as the campaign managers."""
