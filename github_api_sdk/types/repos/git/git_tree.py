

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["GitTree", "Tree"]


class Tree(BaseModel):
    mode: str

    path: str

    sha: str

    type: str

    size: Optional[int] = None

    url: Optional[str] = None


class GitTree(BaseModel):
    sha: str

    tree: List[Tree]
    """Objects specifying a tree structure"""

    truncated: bool

    url: Optional[str] = None
