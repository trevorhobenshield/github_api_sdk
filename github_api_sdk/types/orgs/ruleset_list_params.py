

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RulesetListParams"]


class RulesetListParams(TypedDict, total=False):
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

    targets: str
    """
    A comma-separated list of rule targets to filter by. If provided, only rulesets
    that apply to the specified targets will be returned. For example,
    `branch,tag,push`.
    """
