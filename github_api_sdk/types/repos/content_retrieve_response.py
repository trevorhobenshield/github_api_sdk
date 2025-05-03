

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .content_file import ContentFile

__all__ = [
    "ContentRetrieveResponse",
    "ContentDirectory",
    "ContentDirectory_Links",
    "ContentSymlink",
    "ContentSymlink_Links",
    "ContentSubmodule",
    "ContentSubmodule_Links",
]


class ContentDirectory_Links(BaseModel):
    git: Optional[str] = None

    html: Optional[str] = None

    self: str


class ContentDirectory(BaseModel):
    api_links: ContentDirectory_Links = FieldInfo(alias="_links")

    download_url: Optional[str] = None

    git_url: Optional[str] = None

    html_url: Optional[str] = None

    name: str

    path: str

    sha: str

    size: int

    type: Literal["dir", "file", "submodule", "symlink"]

    url: str

    content: Optional[str] = None


class ContentSymlink_Links(BaseModel):
    git: Optional[str] = None

    html: Optional[str] = None

    self: str


class ContentSymlink(BaseModel):
    api_links: ContentSymlink_Links = FieldInfo(alias="_links")

    download_url: Optional[str] = None

    git_url: Optional[str] = None

    html_url: Optional[str] = None

    name: str

    path: str

    sha: str

    size: int

    target: str

    type: Literal["symlink"]

    url: str


class ContentSubmodule_Links(BaseModel):
    git: Optional[str] = None

    html: Optional[str] = None

    self: str


class ContentSubmodule(BaseModel):
    api_links: ContentSubmodule_Links = FieldInfo(alias="_links")

    download_url: Optional[str] = None

    git_url: Optional[str] = None

    html_url: Optional[str] = None

    name: str

    path: str

    sha: str

    size: int

    submodule_git_url: str

    type: Literal["submodule"]

    url: str


ContentRetrieveResponse: TypeAlias = Union[List[ContentDirectory], ContentFile, ContentSymlink, ContentSubmodule]
