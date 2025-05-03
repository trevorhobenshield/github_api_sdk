

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleRequiredSignaturesParam"]


class RepositoryRuleRequiredSignaturesParam(TypedDict, total=False):
    type: Required[Literal["required_signatures"]]
