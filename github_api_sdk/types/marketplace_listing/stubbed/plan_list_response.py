

from typing import List
from typing_extensions import TypeAlias

from ..marketplace_listing_plan import MarketplaceListingPlan

__all__ = ["PlanListResponse"]

PlanListResponse: TypeAlias = List[MarketplaceListingPlan]
