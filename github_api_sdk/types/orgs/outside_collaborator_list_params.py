

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OutsideCollaboratorListParams"]


class OutsideCollaboratorListParams(TypedDict, total=False):
    filter: Literal["2fa_disabled", "all"]
    """Filter the list of outside collaborators.

    `2fa_disabled` means that only outside collaborators without
    [two-factor authentication](https://github.com/blog/1614-two-factor-authentication)
    enabled will be returned.
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
