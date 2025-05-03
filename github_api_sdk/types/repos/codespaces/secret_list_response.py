

from typing import List

from ...._models import BaseModel
from .repo_codespaces_secret import RepoCodespacesSecret

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    secrets: List[RepoCodespacesSecret]

    total_count: int
