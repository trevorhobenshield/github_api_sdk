

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CopilotGetMetricsParams"]


class CopilotGetMetricsParams(TypedDict, total=False):
    org: Required[str]

    page: int
    """The page number of the results to fetch.

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    per_page: int
    """The number of days of metrics to display per page (max 28).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    since: str
    """Show usage metrics since this date.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
    (`YYYY-MM-DDTHH:MM:SSZ`). Maximum value is 28 days ago.
    """

    until: str
    """Show usage metrics until this date.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
    (`YYYY-MM-DDTHH:MM:SSZ`) and should not preceed the `since` date if it is
    passed.
    """
