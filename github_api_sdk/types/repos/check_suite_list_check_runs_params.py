

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CheckSuiteListCheckRunsParams"]


class CheckSuiteListCheckRunsParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    check_name: str
    """Returns check runs with the specified `name`."""

    filter: Literal["latest", "all"]
    """Filters check runs by their `completed_at` timestamp.

    `latest` returns the most recent check runs.
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

    status: Literal["queued", "in_progress", "completed"]
    """Returns check runs with the specified `status`."""
