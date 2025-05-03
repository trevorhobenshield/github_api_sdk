

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .alert_state import AlertState
from .alert_resolution import AlertResolution

__all__ = ["AlertUpdateParams"]


class AlertUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    state: Required[AlertState]
    """Sets the state of the secret scanning alert.

    You must provide `resolution` when you set the state to `resolved`.
    """

    resolution: AlertResolution | None
    """
    **Required when the `state` is `resolved`.** The reason for resolving the alert.
    """

    resolution_comment: str | None
    """An optional comment when closing an alert.

    Cannot be updated or deleted. Must be `null` when changing `state` to `open`.
    """
