

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleRulesetInfo"]


class RepositoryRuleRulesetInfo(BaseModel):
    ruleset_id: Optional[int] = None
    """The ID of the ruleset that includes this rule."""

    ruleset_source: Optional[str] = None
    """The name of the source of the ruleset that includes this rule."""

    ruleset_source_type: Optional[Literal["Repository", "Organization"]] = None
    """The type of source for the ruleset that includes this rule."""
