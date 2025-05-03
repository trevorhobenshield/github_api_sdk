

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RepoListContributorsParams"]


class RepoListContributorsParams(TypedDict, total=False):
    owner: Required[str]

    anon: str
    """Set to `1` or `true` to include anonymous contributors in results."""

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
