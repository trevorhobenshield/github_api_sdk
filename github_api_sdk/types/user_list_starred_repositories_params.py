

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UserListStarredRepositoriesParams"]


class UserListStarredRepositoriesParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

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
    """The property to sort the results by.

    `created` means when the repository was starred. `updated` means when the
    repository was last pushed to.
    """
