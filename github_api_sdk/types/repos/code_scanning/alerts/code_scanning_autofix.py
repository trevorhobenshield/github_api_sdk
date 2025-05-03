

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["CodeScanningAutofix"]


class CodeScanningAutofix(BaseModel):
    description: Optional[str] = None
    """The description of an autofix."""

    started_at: datetime
    """The start time of an autofix in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."""

    status: Literal["pending", "error", "success", "outdated"]
    """The status of an autofix."""
