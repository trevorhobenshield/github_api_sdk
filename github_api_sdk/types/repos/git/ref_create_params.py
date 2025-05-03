

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RefCreateParams"]


class RefCreateParams(TypedDict, total=False):
    owner: Required[str]

    ref: Required[str]
    """The name of the fully qualified reference (ie: `refs/heads/master`).

    If it doesn't start with 'refs' and have at least two slashes, it will be
    rejected.
    """

    sha: Required[str]
    """The SHA1 value for this reference."""
