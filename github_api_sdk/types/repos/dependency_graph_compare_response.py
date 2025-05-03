

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "DependencyGraphCompareResponse",
    "DependencyGraphCompareResponseItem",
    "DependencyGraphCompareResponseItemVulnerability",
]


class DependencyGraphCompareResponseItemVulnerability(BaseModel):
    advisory_ghsa_id: str

    advisory_summary: str

    advisory_url: str

    severity: str


class DependencyGraphCompareResponseItem(BaseModel):
    change_type: Literal["added", "removed"]

    ecosystem: str

    license: Optional[str] = None

    manifest: str

    name: str

    package_url: Optional[str] = None

    scope: Literal["unknown", "runtime", "development"]
    """Where the dependency is utilized.

    `development` means that the dependency is only utilized in the development
    environment. `runtime` means that the dependency is utilized at runtime and in
    the development environment.
    """

    source_repository_url: Optional[str] = None

    version: str

    vulnerabilities: List[DependencyGraphCompareResponseItemVulnerability]


DependencyGraphCompareResponse: TypeAlias = List[DependencyGraphCompareResponseItem]
