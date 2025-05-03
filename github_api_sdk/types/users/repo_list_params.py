

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RepoListParams"]


class RepoListParams(TypedDict, total=False):
    affiliation: str
    """Comma-separated list of values. Can include:

    - `owner`: Repositories that are owned by the authenticated user.
    - `collaborator`: Repositories that the user has been added to as a
      collaborator.
    - `organization_member`: Repositories that the user has access to through being
      a member of an organization. This includes every repository on every team that
      the user is on.
    """

    before: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only show repositories updated before the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    direction: Literal["asc", "desc"]
    """The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`."""

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

    since: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only show repositories updated after the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    sort: Literal["created", "updated", "pushed", "full_name"]
    """The property to sort the results by."""

    type: Literal["all", "owner", "public", "private", "member"]
    """Limit results to repositories of the specified type.

    Will cause a `422` error if used in the same request as **visibility** or
    **affiliation**.
    """

    visibility: Literal["all", "public", "private"]
    """Limit results to repositories with the specified visibility."""
