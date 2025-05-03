

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RepoSyncWithUpstreamResponse"]


class RepoSyncWithUpstreamResponse(BaseModel):
    base_branch: Optional[str] = None

    merge_type: Optional[Literal["merge", "fast-forward", "none"]] = None

    message: Optional[str] = None
