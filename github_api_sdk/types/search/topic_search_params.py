

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TopicSearchParams"]


class TopicSearchParams(TypedDict, total=False):
    q: Required[str]
    """The query contains one or more search keywords and qualifiers.

    Qualifiers allow you to limit your search to specific areas of GitHub. The REST
    API supports the same qualifiers as the web interface for GitHub. To learn more
    about the format of the query, see
    [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
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
