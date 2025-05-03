

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TimeStatByUserParams"]


class TimeStatByUserParams(TypedDict, total=False):
    org: Required[str]

    min_timestamp: Required[str]
    """The minimum timestamp to query for stats.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    timestamp_increment: Required[str]
    """The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)"""

    max_timestamp: str
    """The maximum timestamp to query for stats.

    Defaults to the time 30 days ago. This is a timestamp in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """
