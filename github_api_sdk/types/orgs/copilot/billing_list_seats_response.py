

from typing import List, Optional

from ...._models import BaseModel
from ..copilot_seat_details import CopilotSeatDetails

__all__ = ["BillingListSeatsResponse"]


class BillingListSeatsResponse(BaseModel):
    seats: Optional[List[CopilotSeatDetails]] = None

    total_seats: Optional[int] = None
    """Total number of Copilot seats for the organization currently being billed."""
