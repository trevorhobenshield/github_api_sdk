

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PersonalAccessTokenListParams"]


class PersonalAccessTokenListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

    last_used_after: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only show fine-grained personal access tokens used after the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    last_used_before: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only show fine-grained personal access tokens used before the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    owner: list[str]
    """A list of owner usernames to use to filter the results."""

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

    permission: str
    """The permission to use to filter the results."""

    repository: str
    """The name of the repository to use to filter the results."""

    sort: Literal["created_at"]
    """The property by which to sort the results."""

    token_id: list[str]
    """The ID of the token"""
