

from typing import List
from typing_extensions import TypeAlias

from ...orgs.packages.package_version import PackageVersion

__all__ = ["VersionListResponse"]

VersionListResponse: TypeAlias = List[PackageVersion]
