

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PackageVersion", "Metadata", "MetadataContainer", "MetadataDocker"]


class MetadataContainer(BaseModel):
    tags: List[str]


class MetadataDocker(BaseModel):
    tag: Optional[List[str]] = None


class Metadata(BaseModel):
    package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"]

    container: Optional[MetadataContainer] = None

    docker: Optional[MetadataDocker] = None


class PackageVersion(BaseModel):
    id: int
    """Unique identifier of the package version."""

    created_at: datetime

    name: str
    """The name of the package version."""

    package_html_url: str

    updated_at: datetime

    url: str

    deleted_at: Optional[datetime] = None

    description: Optional[str] = None

    html_url: Optional[str] = None

    license: Optional[str] = None

    metadata: Optional[Metadata] = None
