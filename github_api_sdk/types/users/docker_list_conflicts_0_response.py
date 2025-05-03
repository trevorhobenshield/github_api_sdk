

from typing import List
from typing_extensions import TypeAlias

from ..orgs.package import Package

__all__ = ["DockerListConflicts0Response"]

DockerListConflicts0Response: TypeAlias = List[Package]
