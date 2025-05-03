

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "CommitBranchesWhereHeadResponse",
    "CommitBranchesWhereHeadResponseItem",
    "CommitBranchesWhereHeadResponseItemCommit",
]


class CommitBranchesWhereHeadResponseItemCommit(BaseModel):
    sha: str

    url: str


class CommitBranchesWhereHeadResponseItem(BaseModel):
    commit: CommitBranchesWhereHeadResponseItemCommit

    name: str

    protected: bool


CommitBranchesWhereHeadResponse: TypeAlias = List[CommitBranchesWhereHeadResponseItem]
