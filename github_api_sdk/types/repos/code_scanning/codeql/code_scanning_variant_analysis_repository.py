

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["CodeScanningVariantAnalysisRepository"]


class CodeScanningVariantAnalysisRepository(BaseModel):
    id: int
    """A unique identifier of the repository."""

    full_name: str
    """The full, globally unique, name of the repository."""

    name: str
    """The name of the repository."""

    private: bool
    """Whether the repository is private."""

    stargazers_count: int

    updated_at: Optional[datetime] = None
