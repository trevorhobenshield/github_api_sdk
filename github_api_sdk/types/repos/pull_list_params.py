

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PullListParams"]


class PullListParams(TypedDict, total=False):
    owner: Required[str]

    base: str
    """Filter pulls by base branch name. Example: `gh-pages`."""

    direction: Literal["asc", "desc"]
    """The direction of the sort.

    Default: `desc` when sort is `created` or sort is not specified, otherwise
    `asc`.
    """

    head: str
    """
    Filter pulls by head user or head organization and branch name in the format of
    `user:ref-name` or `organization:ref-name`. For example:
    `github:new-script-format` or `octocat:test-branch`.
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

    sort: Literal["created", "updated", "popularity", "long-running"]
    """What to sort results by.

    `popularity` will sort by the number of comments. `long-running` will sort by
    date created and will limit the results to pull requests that have been open for
    more than a month and have had activity within the past month.
    """

    state: Literal["open", "closed", "all"]
    """Either `open`, `closed`, or `all` to filter by state."""
