

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRulesetConditionsRepositoryPropertySpecParam"]


class RepositoryRulesetConditionsRepositoryPropertySpecParam(TypedDict, total=False):
    name: Required[str]
    """The name of the repository property to target"""

    property_values: Required[list[str]]
    """The values to match for the repository property"""

    source: Literal["custom", "system"]
    """The source of the repository property. Defaults to 'custom' if not specified."""
