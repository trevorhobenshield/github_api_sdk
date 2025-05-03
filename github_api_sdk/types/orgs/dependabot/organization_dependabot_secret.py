

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OrganizationDependabotSecret"]


class OrganizationDependabotSecret(BaseModel):
    created_at: datetime

    name: str
    """The name of the secret."""

    updated_at: datetime

    visibility: Literal["all", "private", "selected"]
    """Visibility of a secret"""

    selected_repositories_url: Optional[str] = None
