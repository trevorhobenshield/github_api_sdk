

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .code_scanning_alert_dismissed_reason import CodeScanningAlertDismissedReason

__all__ = ["AlertUpdateParams"]


class AlertUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    state: Required[Literal["open", "dismissed"]]
    """Sets the state of the code scanning alert.

    You must provide `dismissed_reason` when you set the state to `dismissed`.
    """

    create_request: bool
    """If `true`, attempt to create an alert dismissal request."""

    dismissed_comment: str | None
    """The dismissal comment associated with the dismissal of the alert."""

    dismissed_reason: CodeScanningAlertDismissedReason | None
    """
    **Required when the state is dismissed.** The reason for dismissing or closing
    the alert.
    """
