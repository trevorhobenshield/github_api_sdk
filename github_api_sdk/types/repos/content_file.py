

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContentFile", "_Links"]


class _Links(BaseModel):
    git: Optional[str] = None

    html: Optional[str] = None

    self: str


class ContentFile(BaseModel):
    api_links: _Links = FieldInfo(alias="_links")

    content: str

    download_url: Optional[str] = None

    encoding: str

    git_url: Optional[str] = None

    html_url: Optional[str] = None

    name: str

    path: str

    sha: str

    size: int

    type: Literal["file"]

    url: str

    submodule_git_url: Optional[str] = None

    target: Optional[str] = None
