

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ImportGetLargeFilesResponse", "ImportGetLargeFilesResponseItem"]


class ImportGetLargeFilesResponseItem(BaseModel):
    oid: str

    path: str

    ref_name: str

    size: int


ImportGetLargeFilesResponse: TypeAlias = List[ImportGetLargeFilesResponseItem]
