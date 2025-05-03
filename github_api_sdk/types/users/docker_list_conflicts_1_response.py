

from typing import List
from typing_extensions import TypeAlias

from ..orgs.package import Package

__all__ = ["DockerListConflicts1Response"]

DockerListConflicts1Response: TypeAlias = List[Package]
