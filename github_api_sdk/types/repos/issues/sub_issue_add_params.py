

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubIssueAddParams"]


class SubIssueAddParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    sub_issue_id: Required[int]
    """The id of the sub-issue to add.

    The sub-issue must belong to the same repository owner as the parent issue
    """

    replace_parent: bool
    """
    Option that, when true, instructs the operation to replace the sub-issues
    current parent issue
    """
