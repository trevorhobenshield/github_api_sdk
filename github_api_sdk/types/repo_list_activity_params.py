

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepoListActivityParams"]


class RepoListActivityParams(TypedDict, total=False):
    owner: Required[str]

    activity_type: Literal["push", "force_push", "branch_creation", "branch_deletion", "pr_merge", "merge_queue_merge"]
    """The activity type to filter by.

    For example, you can choose to filter by "force_push", to see all force pushes
    to the repository.
    """

    actor: str
    """The GitHub username to use to filter by the actor who performed the activity."""

    after: str
    """
    A cursor, as given in the
    [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
    If specified, the query only searches for results after this cursor. For more
    information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    before: str
    """
    A cursor, as given in the
    [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
    If specified, the query only searches for results before this cursor. For more
    information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    ref: str
    """The Git reference for the activities you want to list.

    The `ref` for a branch can be formatted either as `refs/heads/BRANCH_NAME` or
    `BRANCH_NAME`, where `BRANCH_NAME` is the name of your branch.
    """

    time_period: Literal["day", "week", "month", "quarter", "year"]
    """The time period to filter by.

    For example, `day` will filter for activity that occurred in the past 24 hours,
    and `week` will filter for activity that occurred in the past 7 days (168
    hours).
    """
