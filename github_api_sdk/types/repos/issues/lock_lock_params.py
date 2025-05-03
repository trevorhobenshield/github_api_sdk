

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LockLockParams"]


class LockLockParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    lock_reason: Literal["off-topic", "too heated", "resolved", "spam"]
    """The reason for locking the issue or pull request conversation.

    Lock will fail if you don't use one of these reasons:

    - `off-topic`
    - `too heated`
    - `resolved`
    - `spam`
    """
