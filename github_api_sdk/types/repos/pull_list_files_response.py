

from typing import List
from typing_extensions import TypeAlias

from .diff_entry import DiffEntry

__all__ = ["PullListFilesResponse"]

PullListFilesResponse: TypeAlias = List[DiffEntry]
