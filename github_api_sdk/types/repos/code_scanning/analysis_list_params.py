

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnalysisListParams"]


class AnalysisListParams(TypedDict, total=False):
    owner: Required[str]

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

    pr: int
    """The number of the pull request for the results you want to list."""

    ref: str
    """The Git reference for the analyses you want to list.

    The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or
    simply `<branch name>`. To reference a pull request use
    `refs/pull/<number>/merge`.
    """

    sarif_id: str
    """Filter analyses belonging to the same SARIF upload."""

    sort: Literal["created"]
    """The property by which to sort the results."""

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
