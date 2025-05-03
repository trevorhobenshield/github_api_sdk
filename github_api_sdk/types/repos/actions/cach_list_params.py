

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CachListParams"]


class CachListParams(TypedDict, total=False):
    owner: Required[str]

    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

    key: str
    """An explicit key or prefix for identifying the cache"""

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

    ref: str
    """The full Git reference for narrowing down the cache.

    The `ref` for a branch should be formatted as `refs/heads/<branch name>`. To
    reference a pull request use `refs/pull/<number>/merge`.
    """

    sort: Literal["created_at", "last_accessed_at", "size_in_bytes"]
    """The property to sort the results by.

    `created_at` means when the cache was created. `last_accessed_at` means when the
    cache was last accessed. `size_in_bytes` is the size of the cache in bytes.
    """
