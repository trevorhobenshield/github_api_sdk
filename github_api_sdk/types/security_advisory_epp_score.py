

from typing import Optional

from .._models import BaseModel

__all__ = ["SecurityAdvisoryEppScore"]


class SecurityAdvisoryEppScore(BaseModel):
    percentage: Optional[float] = None

    percentile: Optional[float] = None
