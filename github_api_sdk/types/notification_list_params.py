

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NotificationListParams"]


class NotificationListParams(TypedDict, total=False):
    all: bool
    """If `true`, show notifications marked as read."""

    before: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only show notifications updated before the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    page: int
    """The page number of the results to fetch.

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    participating: bool
    """
    If `true`, only shows notifications in which the user is directly participating
    or mentioned.
    """

    per_page: int
    """The number of results per page (max 50).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    since: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only show results that were last updated after the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """
