

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .repos.commit import Commit
from .repos.diff_entry import DiffEntry

__all__ = ["RepoCompareCommitsResponse"]


class RepoCompareCommitsResponse(BaseModel):
    ahead_by: int

    base_commit: Commit
    """Commit"""

    behind_by: int

    commits: List[Commit]

    diff_url: str

    html_url: str

    merge_base_commit: Commit
    """Commit"""

    patch_url: str

    permalink_url: str

    status: Literal["diverged", "ahead", "behind", "identical"]

    total_commits: int

    url: str

    files: Optional[List[DiffEntry]] = None
