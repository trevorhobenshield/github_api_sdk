

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DiscussionListParams"]


class DiscussionListParams(TypedDict, total=False):
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
