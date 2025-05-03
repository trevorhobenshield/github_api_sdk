

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserListIssuesParams"]


class UserListIssuesParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

    filter: Literal["assigned", "created", "mentioned", "subscribed", "repos", "all"]
    """Indicates which sorts of issues to return.

    `assigned` means issues assigned to you. `created` means issues created by you.
    `mentioned` means issues mentioning you. `subscribed` means issues you're
    subscribed to updates for. `all` or `repos` means all issues you can see,
    regardless of participation or creation.
    """

    labels: str
    """A list of comma separated label names. Example: `bug,ui,@high`"""

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
    """Only show results that were last updated after the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    sort: Literal["created", "updated", "comments"]
    """What to sort results by."""

    state: Literal["open", "closed", "all"]
    """Indicates the state of the issues to return."""
