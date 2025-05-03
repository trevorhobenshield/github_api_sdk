

from typing import List

from ...._models import BaseModel
from .codespaces_org_secret import CodespacesOrgSecret

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    secrets: List[CodespacesOrgSecret]

    total_count: int
