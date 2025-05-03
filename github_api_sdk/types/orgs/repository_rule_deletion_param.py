

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleDeletionParam"]


class RepositoryRuleDeletionParam(TypedDict, total=False):
    type: Required[Literal["deletion"]]
