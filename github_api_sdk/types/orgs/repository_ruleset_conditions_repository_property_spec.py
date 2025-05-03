

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRulesetConditionsRepositoryPropertySpec"]


class RepositoryRulesetConditionsRepositoryPropertySpec(BaseModel):
    name: str
    """The name of the repository property to target"""

    property_values: List[str]
    """The values to match for the repository property"""

    source: Optional[Literal["custom", "system"]] = None
    """The source of the repository property. Defaults to 'custom' if not specified."""
