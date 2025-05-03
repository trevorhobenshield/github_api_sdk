

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DiscussionCreateParams"]


class DiscussionCreateParams(TypedDict, total=False):
    org: Required[str]

    body: Required[str]
    """The discussion post's body text."""

    title: Required[str]
    """The discussion post's title."""

    private: bool
    """
    Private posts are only visible to team members, organization owners, and team
    maintainers. Public posts are visible to all members of the organization. Set to
    `true` to create a private post.
    """
