

from typing import Optional

from ..._models import BaseModel

__all__ = ["PullUpdateBranchResponse"]


class PullUpdateBranchResponse(BaseModel):
    message: Optional[str] = None

    url: Optional[str] = None
