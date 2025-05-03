

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleBranchNamePatternParam", "Parameters"]


class Parameters(TypedDict, total=False):
    operator: Required[Literal["starts_with", "ends_with", "contains", "regex"]]
    """The operator to use for matching."""

    pattern: Required[str]
    """The pattern to match with."""

    name: str
    """How this rule will appear to users."""

    negate: bool
    """If true, the rule will fail if the pattern matches."""


class RepositoryRuleBranchNamePatternParam(TypedDict, total=False):
    type: Required[Literal["branch_name_pattern"]]

    parameters: Parameters
