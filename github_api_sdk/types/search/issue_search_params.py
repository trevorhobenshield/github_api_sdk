

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IssueSearchParams"]


class IssueSearchParams(TypedDict, total=False):
    q: Required[str]
    """The query contains one or more search keywords and qualifiers.

    Qualifiers allow you to limit your search to specific areas of GitHub. The REST
    API supports the same qualifiers as the web interface for GitHub. To learn more
    about the format of the query, see
    [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
    See
    "[Searching issues and pull requests](https://docs.github.com/search-github/searching-on-github/searching-issues-and-pull-requests)"
    for a detailed list of qualifiers.
    """

    advanced_search: str
    """
    Set to `true` to use advanced search. Example:
    `http://api.github.com/search/issues?q={query}&advanced_search=true`
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

    sort: Literal[
        "comments",
        "reactions",
        "reactions-+1",
        "reactions--1",
        "reactions-smile",
        "reactions-thinking_face",
        "reactions-heart",
        "reactions-tada",
        "interactions",
        "created",
        "updated",
    ]
    """
    Sorts the results of your query by the number of `comments`, `reactions`,
    `reactions-+1`, `reactions--1`, `reactions-smile`, `reactions-thinking_face`,
    `reactions-heart`, `reactions-tada`, or `interactions`. You can also sort
    results by how recently the items were `created` or `updated`, Default:
    [best match](https://docs.github.com/rest/search/search#ranking-search-results)
    """
