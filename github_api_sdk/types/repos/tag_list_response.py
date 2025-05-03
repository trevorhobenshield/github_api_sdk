

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["TagListResponse", "TagListResponseItem", "TagListResponseItemCommit"]


class TagListResponseItemCommit(BaseModel):
    sha: str

    url: str


class TagListResponseItem(BaseModel):
    commit: TagListResponseItemCommit

    name: str

    node_id: str

    tarball_url: str

    zipball_url: str


TagListResponse: TypeAlias = List[TagListResponseItem]
