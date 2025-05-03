

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PullUpdateParams"]


class PullUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    base: str
    """The name of the branch you want your changes pulled into.

    This should be an existing branch on the current repository. You cannot update
    the base branch on a pull request to point to another repository.
    """

    body: str
    """The contents of the pull request."""

    maintainer_can_modify: bool
    """
    Indicates whether
    [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/)
    the pull request.
    """

    state: Literal["open", "closed"]
    """State of this Pull Request. Either `open` or `closed`."""

    title: str
    """The title of the pull request."""
