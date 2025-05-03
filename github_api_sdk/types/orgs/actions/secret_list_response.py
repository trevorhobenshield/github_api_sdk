

from typing import List

from ...._models import BaseModel
from .organization_secret import OrganizationSecret

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    secrets: List[OrganizationSecret]

    total_count: int
