

from typing import List

from .._models import BaseModel
from .applications.installation import Installation

__all__ = ["OrgListInstallationsResponse"]


class OrgListInstallationsResponse(BaseModel):
    installations: List[Installation]

    total_count: int
