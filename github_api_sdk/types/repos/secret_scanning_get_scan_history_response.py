

from typing import List, Optional

from .scan import Scan
from ..._models import BaseModel

__all__ = ["SecretScanningGetScanHistoryResponse", "CustomPatternBackfillScan"]


class CustomPatternBackfillScan(Scan):
    pattern_name: Optional[str] = None
    """Name of the custom pattern for custom pattern scans"""

    pattern_scope: Optional[str] = None
    """
    Level at which the custom pattern is defined, one of "repository",
    "organization", or "enterprise"
    """


class SecretScanningGetScanHistoryResponse(BaseModel):
    backfill_scans: Optional[List[Scan]] = None

    custom_pattern_backfill_scans: Optional[List[CustomPatternBackfillScan]] = None

    incremental_scans: Optional[List[Scan]] = None

    pattern_update_scans: Optional[List[Scan]] = None
