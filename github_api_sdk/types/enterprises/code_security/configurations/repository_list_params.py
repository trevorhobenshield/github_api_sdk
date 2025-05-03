

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RepositoryListParams"]


class RepositoryListParams(TypedDict, total=False):
    enterprise: Required[str]

    after: str
    """
    A cursor, as given in the
    [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
    If specified, the query only searches for results after this cursor. For more
    information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    before: str
    """
    A cursor, as given in the
    [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
    If specified, the query only searches for results before this cursor. For more
    information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    status: str
    """A comma-separated list of statuses.

    If specified, only repositories with these attachment statuses will be returned.

    Can be: `all`, `attached`, `attaching`, `removed`, `enforced`, `failed`,
    `updating`, `removed_by_enterprise`
    """
