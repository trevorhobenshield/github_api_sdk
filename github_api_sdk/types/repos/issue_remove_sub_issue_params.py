

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IssueRemoveSubIssueParams"]


class IssueRemoveSubIssueParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    sub_issue_id: Required[int]
    """The id of the sub-issue to remove"""
