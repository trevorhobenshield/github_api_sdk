

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IssueListParams"]


class IssueListParams(TypedDict, total=False):
    owner: Required[str]

    assignee: str
    """Can be the name of a user.

    Pass in `none` for issues with no assigned user, and `*` for issues assigned to
    any user.
    """

    creator: str
    """The user that created the issue."""

    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

    labels: str
    """A list of comma separated label names. Example: `bug,ui,@high`"""

    mentioned: str
    """A user that's mentioned in the issue."""

    milestone: str
    """If an `integer` is passed, it should refer to a milestone by its `number` field.

    If the string `*` is passed, issues with any milestone are accepted. If the
    string `none` is passed, issues without milestones are returned.
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

    since: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only show results that were last updated after the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    sort: Literal["created", "updated", "comments"]
    """What to sort results by."""

    state: Literal["open", "closed", "all"]
    """Indicates the state of the issues to return."""

    type: str
    """Can be the name of an issue type.

    If the string `*` is passed, issues with any type are accepted. If the string
    `none` is passed, issues without type are returned.
    """
