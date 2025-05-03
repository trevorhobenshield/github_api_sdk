

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RefUpdateParams"]


class RefUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    sha: Required[str]
    """The SHA1 value to set this reference to"""

    force: bool
    """
    Indicates whether to force the update or to make sure the update is a
    fast-forward update. Leaving this out or setting it to `false` will make sure
    you're not overwriting work.
    """
