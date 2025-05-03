

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RepositoryRulesetConditions", "RefName"]


class RefName(BaseModel):
    exclude: Optional[List[str]] = None
    """Array of ref names or patterns to exclude.

    The condition will not pass if any of these patterns match.
    """

    include: Optional[List[str]] = None
    """Array of ref names or patterns to include.

    One of these patterns must match for the condition to pass. Also accepts
    `~DEFAULT_BRANCH` to include the default branch or `~ALL` to include all
    branches.
    """


class RepositoryRulesetConditions(BaseModel):
    ref_name: Optional[RefName] = None
