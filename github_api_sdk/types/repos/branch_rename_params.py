

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BranchRenameParams"]


class BranchRenameParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    new_name: Required[str]
    """The new name of the branch."""
