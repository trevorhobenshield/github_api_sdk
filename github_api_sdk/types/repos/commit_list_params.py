

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommitListParams"]


class CommitListParams(TypedDict, total=False):
    owner: Required[str]

    author: str
    """GitHub username or email address to use to filter by commit author."""

    committer: str
    """GitHub username or email address to use to filter by commit committer."""

    page: int
    """The page number of the results to fetch.

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    path: str
    """Only commits containing this file path will be returned."""

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    sha: str
    """SHA or branch to start listing commits from.

    Default: the repository’s default branch (usually `main`).
    """

    since: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only show results that were last updated after the given time.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`. Due to limitations of Git, timestamps must be
    between 1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be
    returned.
    """

    until: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Only commits before this date will be returned.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`. Due to limitations of Git, timestamps must be
    between 1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be
    returned.
    """
