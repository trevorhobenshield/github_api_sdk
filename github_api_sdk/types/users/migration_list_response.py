

from typing import TYPE_CHECKING, List
from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from ..orgs.migration import Migration

__all__ = ["MigrationListResponse"]

MigrationListResponse: TypeAlias = List["Migration"]
