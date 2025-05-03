

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleCreationParam"]


class RepositoryRuleCreationParam(TypedDict, total=False):
    type: Required[Literal["creation"]]
