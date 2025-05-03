

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CollaboratorListParams"]


class CollaboratorListParams(TypedDict, total=False):
    affiliation: Literal["outside", "direct", "all"]
    """Filters the collaborators by their affiliation.

    `outside` means outside collaborators of a project that are not a member of the
    project's organization. `direct` means collaborators with permissions to a
    project, regardless of organization membership status. `all` means all
    collaborators the authenticated user can see.
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
