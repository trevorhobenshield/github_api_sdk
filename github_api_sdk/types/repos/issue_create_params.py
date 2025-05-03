

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["IssueCreateParams", "Label", "LabelUnionMember1"]


class IssueCreateParams(TypedDict, total=False):
    owner: Required[str]

    title: Required[str | int]
    """The title of the issue."""

    assignee: str | None
    """Login for the user that this issue should be assigned to.

    _NOTE: Only users with push access can set the assignee for new issues. The
    assignee is silently dropped otherwise. **This field is closing down.**_
    """

    assignees: list[str]
    """Logins for Users to assign to this issue.

    _NOTE: Only users with push access can set assignees for new issues. Assignees
    are silently dropped otherwise._
    """

    body: str
    """The contents of the issue."""

    labels: list[Label]
    """Labels to associate with this issue.

    _NOTE: Only users with push access can set labels for new issues. Labels are
    silently dropped otherwise._
    """

    milestone: str | int | None
    """The `number` of the milestone to associate this issue with.

    _NOTE: Only users with push access can set the milestone for new issues. The
    milestone is silently dropped otherwise._
    """

    type: str | None
    """The name of the issue type to associate with this issue.

    _NOTE: Only users with push access can set the type for new issues. The type is
    silently dropped otherwise._
    """


class LabelUnionMember1(TypedDict, total=False):
    id: int

    color: str | None

    description: str | None

    name: str


Label: TypeAlias = Union[str, LabelUnionMember1]
