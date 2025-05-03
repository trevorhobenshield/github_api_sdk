

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["APIUserStatsParams"]


class APIUserStatsParams(TypedDict, total=False):
    org: Required[str]

    min_timestamp: Required[str]
    """The minimum timestamp to query for stats.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    actor_name_substring: str
    """
    Providing a substring will filter results where the actor name contains the
    substring. This is a case-insensitive search.
    """

    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

    max_timestamp: str
    """The maximum timestamp to query for stats.

    Defaults to the time 30 days ago. This is a timestamp in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    page: int
    """The page number of the results to fetch.

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    sort: list[
        Literal[
            "last_rate_limited_timestamp",
            "last_request_timestamp",
            "rate_limited_request_count",
            "subject_name",
            "total_request_count",
        ]
    ]
    """The property to sort the results by."""
