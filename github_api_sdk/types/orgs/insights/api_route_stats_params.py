

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["APIRouteStatsParams"]


class APIRouteStatsParams(TypedDict, total=False):
    org: Required[str]

    actor_type: Required[
        Literal["installation", "classic_pat", "fine_grained_pat", "oauth_app", "github_app_user_to_server"]
    ]

    min_timestamp: Required[str]
    """The minimum timestamp to query for stats.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    api_route_substring: str
    """
    Providing a substring will filter results where the API route contains the
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
            "http_method",
            "api_route",
            "total_request_count",
        ]
    ]
    """The property to sort the results by."""
