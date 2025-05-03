

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .state import State

__all__ = ["CampaignListParams"]


class CampaignListParams(TypedDict, total=False):
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

    sort: Literal["created", "updated", "ends_at", "published"]
    """The property by which to sort the results."""

    state: State
    """If specified, only campaigns with this state will be returned."""
