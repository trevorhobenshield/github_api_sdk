

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["MigrationListParams"]


class MigrationListParams(TypedDict, total=False):
    exclude: list[Literal["repositories"]]
    """Exclude attributes from the API response to improve performance"""

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
