

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LabelSearchParams"]


class LabelSearchParams(TypedDict, total=False):
    q: Required[str]
    """The search keywords.

    This endpoint does not accept qualifiers in the query. To learn more about the
    format of the query, see
    [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
    """

    repository_id: Required[int]
    """The id of the repository."""

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

    sort: Literal["created", "updated"]
    """Sorts the results of your query by when the label was `created` or `updated`.

    Default:
    [best match](https://docs.github.com/rest/search/search#ranking-search-results)
    """
