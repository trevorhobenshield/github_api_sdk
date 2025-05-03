

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """To return the oldest accounts first, set to `asc`.

    Ignored without the `sort` parameter.
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
    """The property to sort the results by."""
