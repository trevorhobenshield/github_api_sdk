

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PullUpdateBranchParams"]


class PullUpdateBranchParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    expected_head_sha: str
    """The expected SHA of the pull request's HEAD ref.

    This is the most recent commit on the pull request's branch. If the expected SHA
    does not match the pull request's HEAD, you will receive a
    `422 Unprocessable Entity` status. You can use the
    "[List commits](https://docs.github.com/rest/commits/commits#list-commits)"
    endpoint to find the most recent commit SHA. Default: SHA of the pull request's
    current HEAD ref.
    """
