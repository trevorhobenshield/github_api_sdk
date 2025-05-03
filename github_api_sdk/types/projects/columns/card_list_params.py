

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    archived_state: Literal["all", "archived", "not_archived"]
    """Filters the project cards that are returned by the card's state."""

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
