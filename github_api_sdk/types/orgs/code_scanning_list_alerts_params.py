

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .alert_severity import AlertSeverity
from .alert_state_query import AlertStateQuery

__all__ = ["CodeScanningListAlertsParams"]


class CodeScanningListAlertsParams(TypedDict, total=False):
    after: str
    """
    A cursor, as given in the
    [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
    If specified, the query only searches for results after this cursor. For more
    information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    before: str
    """
    A cursor, as given in the
    [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
    If specified, the query only searches for results before this cursor. For more
    information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

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

    severity: AlertSeverity
    """If specified, only code scanning alerts with this severity will be returned."""

    sort: Literal["created", "updated"]
    """The property by which to sort the results."""

    state: AlertStateQuery
    """If specified, only code scanning alerts with this state will be returned."""

    tool_guid: str | None
    """The GUID of a code scanning tool.

    Only results by this tool will be listed. Note that some code scanning tools may
    not include a GUID in their analysis data. You can specify the tool by using
    either `tool_guid` or `tool_name`, but not both.
    """

    tool_name: str
    """The name of a code scanning tool.

    Only results by this tool will be listed. You can specify the tool by using
    either `tool_name` or `tool_guid`, but not both.
    """
