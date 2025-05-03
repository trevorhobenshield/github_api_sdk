

from typing import List
from typing_extensions import TypeAlias

from ..minimal_repository import MinimalRepository

__all__ = ["MigrationListRepositoriesResponse"]

MigrationListRepositoriesResponse: TypeAlias = List[MinimalRepository]
