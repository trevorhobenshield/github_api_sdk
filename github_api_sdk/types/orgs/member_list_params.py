

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    filter: Literal["2fa_disabled", "all"]
    """Filter members returned in the list.

    `2fa_disabled` means that only members without
    [two-factor authentication](https://github.com/blog/1614-two-factor-authentication)
    enabled will be returned. This options is only available for organization
    owners.
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

    role: Literal["all", "admin", "member"]
    """Filter members returned by their role."""
