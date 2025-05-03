

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeliveryListParams"]


class DeliveryListParams(TypedDict, total=False):
    org: Required[str]

    cursor: str
    """
    Used for pagination: the starting delivery from which the page of deliveries is
    fetched. Refer to the `link` header for the next and previous page cursors.
    """

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """
