

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RepoListParams"]


class RepoListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`."""

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

    sort: Literal["created", "updated", "pushed", "full_name"]
    """The property to sort the results by."""

    type: Literal["all", "public", "private", "forks", "sources", "member"]
    """Specifies the types of repositories you want returned."""
