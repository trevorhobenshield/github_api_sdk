

from typing import List
from typing_extensions import TypeAlias

from ..orgs.package import Package

__all__ = ["PackageListResponse"]

PackageListResponse: TypeAlias = List[Package]
