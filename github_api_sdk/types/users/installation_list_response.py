

from typing import TYPE_CHECKING, List

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..applications.installation import Installation

__all__ = ["InstallationListResponse"]


class InstallationListResponse(BaseModel):
    installations: List["Installation"]

    total_count: int
