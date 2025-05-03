

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositorySearchParams"]


class RepositorySearchParams(TypedDict, total=False):
    q: Required[str]
    """The query contains one or more search keywords and qualifiers.

    Qualifiers allow you to limit your search to specific areas of GitHub. The REST
    API supports the same qualifiers as the web interface for GitHub. To learn more
    about the format of the query, see
    [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
    See
    "[Searching for repositories](https://docs.github.com/articles/searching-for-repositories/)"
    for a detailed list of qualifiers.
    """

    order: Literal["desc", "asc"]
    """
    Determines whether the first search result returned is the highest number of
    matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
    unless you provide `sort`.
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

    sort: Literal["stars", "forks", "help-wanted-issues", "updated"]
    """
    Sorts the results of your query by number of `stars`, `forks`, or
    `help-wanted-issues` or how recently the items were `updated`. Default:
    [best match](https://docs.github.com/rest/search/search#ranking-search-results)
    """
