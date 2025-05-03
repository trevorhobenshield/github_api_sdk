

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BranchListParams"]


class BranchListParams(TypedDict, total=False):
    owner: Required[str]

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

    protected: bool
    """
    Setting to `true` returns only branches protected by branch protections or
    rulesets. When set to `false`, only unprotected branches are returned. Omitting
    this parameter returns all branches.
    """
