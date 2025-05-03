

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    owner: Required[str]

    environment: str | None
    """
    The name of the environment that was deployed to (e.g., `staging` or
    `production`).
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

    ref: str
    """The name of the ref. This can be a branch, tag, or SHA."""

    sha: str
    """The SHA recorded at creation time."""

    task: str
    """
    The name of the task for the deployment (e.g., `deploy` or `deploy:migrations`).
    """
