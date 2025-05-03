

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["IssueUpdateParams", "Label", "LabelUnionMember1"]


class IssueUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    assignee: str | None
    """Username to assign to this issue. **This field is closing down.**"""

    assignees: list[str]
    """Usernames to assign to this issue.

    Pass one or more user logins to _replace_ the set of assignees on this issue.
    Send an empty array (`[]`) to clear all assignees from the issue. Only users
    with push access can set assignees for new issues. Without push access to the
    repository, assignee changes are silently dropped.
    """

    body: str | None
    """The contents of the issue."""

    labels: list[Label]
    """Labels to associate with this issue.

    Pass one or more labels to _replace_ the set of labels on this issue. Send an
    empty array (`[]`) to clear all labels from the issue. Only users with push
    access can set labels for issues. Without push access to the repository, label
    changes are silently dropped.
    """

    milestone: str | int | None
    """
    The `number` of the milestone to associate this issue with or use `null` to
    remove the current milestone. Only users with push access can set the milestone
    for issues. Without push access to the repository, milestone changes are
    silently dropped.
    """

    state: Literal["open", "closed"]
    """The open or closed state of the issue."""

    state_reason: Literal["completed", "not_planned", "reopened"] | None
    """The reason for the state change. Ignored unless `state` is changed."""

    title: str | int | None
    """The title of the issue."""

    type: str | None
    """
    The name of the issue type to associate with this issue or use `null` to remove
    the current issue type. Only users with push access can set the type for issues.
    Without push access to the repository, type changes are silently dropped.
    """


class LabelUnionMember1(TypedDict, total=False):
    id: int

    color: str | None

    description: str | None

    name: str


Label: TypeAlias = Union[str, LabelUnionMember1]
