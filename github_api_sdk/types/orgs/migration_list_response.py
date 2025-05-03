

from typing import List
from typing_extensions import TypeAlias

from .migration import Migration

__all__ = ["MigrationListResponse"]

MigrationListResponse: TypeAlias = List[Migration]
