

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["WorkflowListRunsParams"]


class WorkflowListRunsParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    actor: str
    """Returns someone's workflow runs.

    Use the login for the user who created the `push` associated with the check
    suite or workflow run.
    """

    branch: str
    """Returns workflow runs associated with a branch.

    Use the name of the branch of the `push`.
    """

    check_suite_id: int
    """Returns workflow runs with the `check_suite_id` that you specify."""

    created: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """Returns workflow runs created within the given date-time range.

    For more information on the syntax, see
    "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."
    """

    event: str
    """Returns workflow run triggered by the event you specify.

    For example, `push`, `pull_request` or `issue`. For more information, see
    "[Events that trigger workflows](https://docs.github.com/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows)."
    """

    exclude_pull_requests: bool
    """If `true` pull requests are omitted from the response (empty array)."""

    head_sha: str
    """Only returns workflow runs that are associated with the specified `head_sha`."""

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

    status: Literal[
        "completed",
        "action_required",
        "cancelled",
        "failure",
        "neutral",
        "skipped",
        "stale",
        "success",
        "timed_out",
        "in_progress",
        "queued",
        "requested",
        "waiting",
        "pending",
    ]
    """
    Returns workflow runs with the check run `status` or `conclusion` that you
    specify. For example, a conclusion can be `success` or a status can be
    `in_progress`. Only GitHub Actions can set a status of `waiting`, `pending`, or
    `requested`.
    """
