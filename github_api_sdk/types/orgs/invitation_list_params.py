

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InvitationListParams"]


class InvitationListParams(TypedDict, total=False):
    invitation_source: Literal["all", "member", "scim"]
    """Filter invitations by their invitation source."""

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

    role: Literal["all", "admin", "direct_member", "billing_manager", "hiring_manager"]
    """Filter invitations by their member role."""
