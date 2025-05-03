

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PersonalAccessTokenUpdateParams"]


class PersonalAccessTokenUpdateParams(TypedDict, total=False):
    action: Required[Literal["revoke"]]
    """Action to apply to the fine-grained personal access token."""

    pat_ids: Required[Iterable[int]]
    """The IDs of the fine-grained personal access tokens."""
