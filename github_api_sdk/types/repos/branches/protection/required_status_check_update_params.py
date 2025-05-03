

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RequiredStatusCheckUpdateParams", "Check"]


class RequiredStatusCheckUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    checks: Iterable[Check]
    """The list of status checks to require in order to merge into this branch."""

    contexts: list[str]
    """
    **Closing down notice**: The list of status checks to require in order to merge
    into this branch. If any of these checks have recently been set by a particular
    GitHub App, they will be required to come from that app in future for the branch
    to merge. Use `checks` instead of `contexts` for more fine-grained control.
    """

    strict: bool
    """Require branches to be up to date before merging."""


class Check(TypedDict, total=False):
    context: Required[str]
    """The name of the required check"""

    app_id: int
    """The ID of the GitHub App that must provide this check.

    Omit this field to automatically select the GitHub App that has recently
    provided this check, or any app if it was not set by a GitHub App. Pass -1 to
    explicitly allow any app to set the status.
    """
