

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SubUpdateParams"]


class SubUpdateParams(TypedDict, total=False):
    owner: Required[str]

    use_default: Required[bool]
    """Whether to use the default template or not.

    If `true`, the `include_claim_keys` field is ignored.
    """

    include_claim_keys: list[str]
    """Array of unique strings.

    Each claim key can only contain alphanumeric characters and underscores.
    """
