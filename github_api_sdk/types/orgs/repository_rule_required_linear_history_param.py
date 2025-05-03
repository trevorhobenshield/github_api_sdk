

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleRequiredLinearHistoryParam"]


class RepositoryRuleRequiredLinearHistoryParam(TypedDict, total=False):
    type: Required[Literal["required_linear_history"]]
