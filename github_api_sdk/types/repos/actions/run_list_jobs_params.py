

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RunListJobsParams"]


class RunListJobsParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    filter: Literal["latest", "all"]
    """Filters jobs by their `completed_at` timestamp.

    `latest` returns jobs from the most recent execution of the workflow run. `all`
    returns all jobs for a workflow run, including from old executions of the
    workflow run.
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
