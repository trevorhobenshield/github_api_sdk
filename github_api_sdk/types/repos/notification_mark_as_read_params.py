

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NotificationMarkAsReadParams"]


class NotificationMarkAsReadParams(TypedDict, total=False):
    owner: Required[str]

    last_read_at: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Describes the last point that notifications were checked.

    Anything updated since this time will not be marked as read. If you omit this
    parameter, all notifications are marked as read. This is a timestamp in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
    `YYYY-MM-DDTHH:MM:SSZ`. Default: The current timestamp.
    """
