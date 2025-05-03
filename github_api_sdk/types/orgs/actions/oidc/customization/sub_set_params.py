

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SubSetParams"]


class SubSetParams(TypedDict, total=False):
    include_claim_keys: Required[list[str]]
    """Array of unique strings.

    Each claim key can only contain alphanumeric characters and underscores.
    """
