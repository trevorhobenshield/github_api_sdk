

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MigrationRetrieveStatusParams"]


class MigrationRetrieveStatusParams(TypedDict, total=False):
    org: Required[str]

    exclude: list[Literal["repositories"]]
    """Exclude attributes from the API response to improve performance"""
