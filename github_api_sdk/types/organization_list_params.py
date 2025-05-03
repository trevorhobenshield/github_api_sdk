

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OrganizationListParams"]


class OrganizationListParams(TypedDict, total=False):
    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    since: int
    """An organization ID. Only return organizations with an ID greater than this ID."""
