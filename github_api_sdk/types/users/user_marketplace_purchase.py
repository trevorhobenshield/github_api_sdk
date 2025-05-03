

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..marketplace_listing.marketplace_listing_plan import MarketplaceListingPlan

__all__ = ["UserMarketplacePurchase", "Account"]


class Account(BaseModel):
    id: int

    login: str

    type: str

    url: str

    email: Optional[str] = None

    node_id: Optional[str] = None

    organization_billing_email: Optional[str] = None


class UserMarketplacePurchase(BaseModel):
    account: Account

    billing_cycle: str

    free_trial_ends_on: Optional[datetime] = None

    next_billing_date: Optional[datetime] = None

    on_free_trial: bool

    plan: MarketplaceListingPlan
    """Marketplace Listing Plan"""

    unit_count: Optional[int] = None

    updated_at: Optional[datetime] = None
