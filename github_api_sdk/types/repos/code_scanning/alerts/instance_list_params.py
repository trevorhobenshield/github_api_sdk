

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceListParams"]


class InstanceListParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

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

    pr: int
    """The number of the pull request for the results you want to list."""

    ref: str
    """The Git reference for the results you want to list.

    The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or
    simply `<branch name>`. To reference a pull request use
    `refs/pull/<number>/merge`.
    """
