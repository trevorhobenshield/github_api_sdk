

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DiffEntry"]


class DiffEntry(BaseModel):
    additions: int

    blob_url: str

    changes: int

    contents_url: str

    deletions: int

    filename: str

    raw_url: str

    sha: str

    status: Literal["added", "removed", "modified", "renamed", "copied", "changed", "unchanged"]

    patch: Optional[str] = None

    previous_filename: Optional[str] = None
