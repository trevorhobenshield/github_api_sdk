

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RunnerGroupListParams"]


class RunnerGroupListParams(TypedDict, total=False):
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

    visible_to_repository: str
    """Only return runner groups that are allowed to be used by this repository."""
