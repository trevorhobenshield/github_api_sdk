

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MarketplaceListingPlan"]


class MarketplaceListingPlan(BaseModel):
    id: int

    accounts_url: str

    bullets: List[str]

    description: str

    has_free_trial: bool

    monthly_price_in_cents: int

    name: str

    number: int

    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"]

    state: str

    unit_name: Optional[str] = None

    url: str

    yearly_price_in_cents: int
