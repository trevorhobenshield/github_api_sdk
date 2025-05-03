

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .orgs.nullable_license_simple import NullableLicenseSimple

__all__ = ["RepoGetLicenseResponse", "_Links"]


class _Links(BaseModel):
    git: Optional[str] = None

    html: Optional[str] = None

    self: str


class RepoGetLicenseResponse(BaseModel):
    api_links: _Links = FieldInfo(alias="_links")

    content: str

    download_url: Optional[str] = None

    encoding: str

    git_url: Optional[str] = None

    html_url: Optional[str] = None

    license: Optional[NullableLicenseSimple] = None
    """License Simple"""

    name: str

    path: str

    sha: str

    size: int

    type: str

    url: str
