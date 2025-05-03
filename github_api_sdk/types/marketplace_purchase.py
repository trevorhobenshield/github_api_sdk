
from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .marketplace_listing.marketplace_listing_plan import MarketplaceListingPlan

__all__ = ["MarketplacePurchase", "MarketplacePendingChange"]


class MarketplacePendingChange(BaseModel):
    id: int | None = None

    effective_date: str | None = None

    is_installed: bool | None = None

    plan: MarketplaceListingPlan | None = None
    """Marketplace Listing Plan"""

    unit_count: int | None = None


class MarketplacePurchase(BaseModel):
    id: int

    login: str

    marketplace_purchase: MarketplacePurchase

    type: str

    url: str

    email: str | None = None

    marketplace_pending_change: MarketplacePendingChange | None = None

    organization_billing_email: str | None = None
