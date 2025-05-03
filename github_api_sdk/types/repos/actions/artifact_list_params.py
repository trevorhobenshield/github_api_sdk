

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ArtifactListParams"]


class ArtifactListParams(TypedDict, total=False):
    owner: Required[str]

    name: str
    """The name field of an artifact.

    When specified, only artifacts with this name will be returned.
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
