

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RepoMergeBranchParams"]


class RepoMergeBranchParams(TypedDict, total=False):
    owner: Required[str]

    base: Required[str]
    """The name of the base branch that the head will be merged into."""

    head: Required[str]
    """The head to merge. This can be a branch name or a commit SHA1."""

    commit_message: str
    """Commit message to use for the merge commit.

    If omitted, a default message will be used.
    """
