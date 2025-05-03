

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .branches.branch_protection import BranchProtection

__all__ = ["BranchListResponse", "BranchListResponseItem", "BranchListResponseItemCommit"]


class BranchListResponseItemCommit(BaseModel):
    sha: str

    url: str


class BranchListResponseItem(BaseModel):
    commit: BranchListResponseItemCommit

    name: str

    protected: bool

    protection: Optional[BranchProtection] = None
    """Branch Protection"""

    protection_url: Optional[str] = None


BranchListResponse: TypeAlias = List[BranchListResponseItem]
