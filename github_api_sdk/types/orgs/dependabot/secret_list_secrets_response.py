

from typing import List

from ...._models import BaseModel
from .organization_dependabot_secret import OrganizationDependabotSecret

__all__ = ["SecretListSecretsResponse"]


class SecretListSecretsResponse(BaseModel):
    secrets: List[OrganizationDependabotSecret]

    total_count: int
