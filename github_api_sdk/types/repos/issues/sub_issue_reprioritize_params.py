

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubIssueReprioritizeParams"]


class SubIssueReprioritizeParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    sub_issue_id: Required[int]
    """The id of the sub-issue to reprioritize"""

    after_id: int
    """
    The id of the sub-issue to be prioritized after (either positional argument
    after OR before should be specified).
    """

    before_id: int
    """
    The id of the sub-issue to be prioritized before (either positional argument
    after OR before should be specified).
    """
