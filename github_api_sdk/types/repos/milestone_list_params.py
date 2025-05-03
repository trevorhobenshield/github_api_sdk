

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MilestoneListParams"]


class MilestoneListParams(TypedDict, total=False):
    owner: Required[str]

    direction: Literal["asc", "desc"]
    """The direction of the sort. Either `asc` or `desc`."""

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

    sort: Literal["due_on", "completeness"]
    """What to sort results by. Either `due_on` or `completeness`."""

    state: Literal["open", "closed", "all"]
    """The state of the milestone. Either `open`, `closed`, or `all`."""
