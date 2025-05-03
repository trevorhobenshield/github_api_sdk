

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserSearchParams"]


class UserSearchParams(TypedDict, total=False):
    q: Required[str]
    """The query contains one or more search keywords and qualifiers.

    Qualifiers allow you to limit your search to specific areas of GitHub. The REST
    API supports the same qualifiers as the web interface for GitHub. To learn more
    about the format of the query, see
    [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
    See
    "[Searching users](https://docs.github.com/search-github/searching-on-github/searching-users)"
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

    sort: Literal["followers", "repositories", "joined"]
    """
    Sorts the results of your query by number of `followers` or `repositories`, or
    when the person `joined` GitHub. Default:
    [best match](https://docs.github.com/rest/search/search#ranking-search-results)
    """
