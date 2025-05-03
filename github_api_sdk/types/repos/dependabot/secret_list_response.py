

from typing import List

from ...._models import BaseModel
from .dependabot_secret import DependabotSecret

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    secrets: List[DependabotSecret]

    total_count: int
