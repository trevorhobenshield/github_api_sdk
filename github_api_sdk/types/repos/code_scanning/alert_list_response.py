

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ...._models import BaseModel
from ...applications.user import User
from ...orgs.alert_rule_summary import AlertRuleSummary
from .code_scanning_alert_state import CodeScanningAlertState
from .code_scanning_analysis_tool import CodeScanningAnalysisTool
from .code_scanning_alert_instance import CodeScanningAlertInstance
from .code_scanning_alert_dismissed_reason import CodeScanningAlertDismissedReason

__all__ = ["AlertListResponse", "AlertListResponseItem"]


class AlertListResponseItem(BaseModel):
    created_at: datetime
    """The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."""

    dismissed_at: Optional[datetime] = None
    """
    The time that the alert was dismissed in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    dismissed_by: Optional[User] = None
    """A GitHub user."""

    dismissed_reason: Optional[CodeScanningAlertDismissedReason] = None
    """
    **Required when the state is dismissed.** The reason for dismissing or closing
    the alert.
    """

    html_url: str
    """The GitHub URL of the alert resource."""

    instances_url: str
    """The REST API URL for fetching the list of instances for an alert."""

    most_recent_instance: CodeScanningAlertInstance

    number: int
    """The security alert number."""

    rule: AlertRuleSummary

    state: Optional[CodeScanningAlertState] = None
    """State of a code scanning alert."""

    tool: CodeScanningAnalysisTool

    url: str
    """The REST API URL of the alert resource."""

    dismissal_approved_by: Optional[User] = None
    """A GitHub user."""

    dismissed_comment: Optional[str] = None
    """The dismissal comment associated with the dismissal of the alert."""

    fixed_at: Optional[datetime] = None
    """
    The time that the alert was no longer detected and was considered fixed in ISO
    8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    updated_at: Optional[datetime] = None
    """
    The time that the alert was last updated in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """


AlertListResponse: TypeAlias = List[AlertListResponseItem]
