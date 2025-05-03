

from typing import List
from typing_extensions import TypeAlias

from .package_version import PackageVersion

__all__ = ["VersionListResponse"]

VersionListResponse: TypeAlias = List[PackageVersion]
