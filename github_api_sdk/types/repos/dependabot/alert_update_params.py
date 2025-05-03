

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertUpdateParams"]


class AlertUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    state: Required[Literal["dismissed", "open"]]
    """
    The state of the Dependabot alert. A `dismissed_reason` must be provided when
    setting the state to `dismissed`.
    """

    dismissed_comment: str
    """An optional comment associated with dismissing the alert."""

    dismissed_reason: Literal["fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"]
    """**Required when `state` is `dismissed`.** A reason for dismissing the alert."""
