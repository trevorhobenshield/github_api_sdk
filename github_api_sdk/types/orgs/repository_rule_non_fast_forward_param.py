

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleNonFastForwardParam"]


class RepositoryRuleNonFastForwardParam(TypedDict, total=False):
    type: Required[Literal["non_fast_forward"]]
