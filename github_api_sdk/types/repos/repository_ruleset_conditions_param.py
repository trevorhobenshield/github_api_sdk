

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["RepositoryRulesetConditionsParam", "RefName"]


class RefName(TypedDict, total=False):
    exclude: list[str]
    """Array of ref names or patterns to exclude.

    The condition will not pass if any of these patterns match.
    """

    include: list[str]
    """Array of ref names or patterns to include.

    One of these patterns must match for the condition to pass. Also accepts
    `~DEFAULT_BRANCH` to include the default branch or `~ALL` to include all
    branches.
    """


class RepositoryRulesetConditionsParam(TypedDict, total=False):
    ref_name: RefName
