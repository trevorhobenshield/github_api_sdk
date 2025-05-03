

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollaboratorListParams"]


class CollaboratorListParams(TypedDict, total=False):
    owner: Required[str]

    affiliation: Literal["outside", "direct", "all"]
    """Filter collaborators returned by their affiliation.

    `outside` means all outside collaborators of an organization-owned repository.
    `direct` means all collaborators with permissions to an organization-owned
    repository, regardless of organization membership status. `all` means all
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

    permission: Literal["pull", "triage", "push", "maintain", "admin"]
    """Filter collaborators by the permissions they have on the repository.

    If not specified, all collaborators will be returned.
    """
