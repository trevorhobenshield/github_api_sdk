

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepoCreateCommitStatusParams"]


class RepoCreateCommitStatusParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    state: Required[Literal["error", "failure", "pending", "success"]]
    """The state of the status."""

    context: str
    """A string label to differentiate this status from the status of other systems.

    This field is case-insensitive.
    """

    description: str | None
    """A short description of the status."""

    target_url: str | None
    """The target URL to associate with this status.

    This URL will be linked from the GitHub UI to allow users to easily see the
    source of the status.  
    For example, if your continuous integration system is posting build status, you
    would want to provide the deep link for the build output for this specific
    SHA:  
    `http://ci.example.com/user/repo/build/sha`
    """
