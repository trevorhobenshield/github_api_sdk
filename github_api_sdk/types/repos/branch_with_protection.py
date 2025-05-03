

from typing import Optional

from pydantic import Field as FieldInfo

from .commit import Commit
from ..._models import BaseModel
from .branches.branch_protection import BranchProtection

__all__ = ["BranchWithProtection", "_Links"]


class _Links(BaseModel):
    html: str

    self: str


class BranchWithProtection(BaseModel):
    api_links: _Links = FieldInfo(alias="_links")

    commit: Commit
    """Commit"""

    name: str

    protected: bool

    protection: BranchProtection
    """Branch Protection"""

    protection_url: str

    pattern: Optional[str] = None

    required_approving_review_count: Optional[int] = None
