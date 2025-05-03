

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleBranchNamePattern", "Parameters"]


class Parameters(BaseModel):
    operator: Literal["starts_with", "ends_with", "contains", "regex"]
    """The operator to use for matching."""

    pattern: str
    """The pattern to match with."""

    name: Optional[str] = None
    """How this rule will appear to users."""

    negate: Optional[bool] = None
    """If true, the rule will fail if the pattern matches."""


class RepositoryRuleBranchNamePattern(BaseModel):
    type: Literal["branch_name_pattern"]

    parameters: Optional[Parameters] = None
