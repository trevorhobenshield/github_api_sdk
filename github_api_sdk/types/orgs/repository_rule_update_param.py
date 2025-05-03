

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleUpdateParam", "Parameters"]


class Parameters(TypedDict, total=False):
    update_allows_fetch_and_merge: Required[bool]
    """Branch can pull changes from its upstream repository"""


class RepositoryRuleUpdateParam(TypedDict, total=False):
    type: Required[Literal["update"]]

    parameters: Parameters
