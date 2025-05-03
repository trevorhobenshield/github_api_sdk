

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CodeSearchParams"]


class CodeSearchParams(TypedDict, total=False):
    q: Required[str]
    """The query contains one or more search keywords and qualifiers.

    Qualifiers allow you to limit your search to specific areas of GitHub. The REST
    API supports the same qualifiers as the web interface for GitHub. To learn more
    about the format of the query, see
    [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
    See
    "[Searching code](https://docs.github.com/search-github/searching-on-github/searching-code)"
    for a detailed list of qualifiers.
    """

    order: Literal["desc", "asc"]
    """
    **This field is closing down.** Determines whether the first search result
    returned is the highest number of matches (`desc`) or lowest number of matches
    (`asc`). This parameter is ignored unless you provide `sort`.
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

    sort: Literal["indexed"]
    """**This field is closing down.** Sorts the results of your query.

    Can only be `indexed`, which indicates how recently a file has been indexed by
    the GitHub search infrastructure. Default:
    [best match](https://docs.github.com/rest/search/search#ranking-search-results)
    """
