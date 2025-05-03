

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["MigrationRetrieveParams"]


class MigrationRetrieveParams(TypedDict, total=False):
    exclude: list[str]
