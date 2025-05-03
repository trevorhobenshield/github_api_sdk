

from typing import List
from typing_extensions import TypeAlias

from .package import Package

__all__ = ["DockerListConflictsResponse"]

DockerListConflictsResponse: TypeAlias = List[Package]
