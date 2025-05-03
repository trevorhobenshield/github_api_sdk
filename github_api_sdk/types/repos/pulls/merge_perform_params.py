

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MergePerformParams"]


class MergePerformParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    commit_message: str
    """Extra detail to append to automatic commit message."""

    commit_title: str
    """Title for the automatic commit message."""

    merge_method: Literal["merge", "squash", "rebase"]
    """The merge method to use."""

    sha: str
    """SHA that pull request head must match to allow merge."""
