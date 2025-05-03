

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CampaignCreateParams", "CodeScanningAlert"]


class CampaignCreateParams(TypedDict, total=False):
    code_scanning_alerts: Required[Iterable[CodeScanningAlert]]
    """The code scanning alerts to include in this campaign"""

    description: Required[str]
    """A description for the campaign"""

    ends_at: Required[Annotated[str | datetime, PropertyInfo(format="iso8601")]]
    """The end date and time of the campaign. The date must be in the future."""

    name: Required[str]
    """The name of the campaign"""

    contact_link: str | None
    """The contact link of the campaign. Must be a URI."""

    generate_issues: bool
    """If true, will automatically generate issues for the campaign.

    The default is false.
    """

    managers: list[str]
    """The logins of the users to set as the campaign managers.

    At this time, only a single manager can be supplied.
    """

    team_managers: list[str]
    """The slugs of the teams to set as the campaign managers."""


class CodeScanningAlert(TypedDict, total=False):
    alert_numbers: Required[Iterable[int]]
    """The alert numbers"""

    repository_id: Required[int]
    """The repository id"""
