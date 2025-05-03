

from typing import List
from typing_extensions import TypeAlias

from .user_marketplace_purchase import UserMarketplacePurchase

__all__ = ["MarketplacePurchaseListResponse"]

MarketplacePurchaseListResponse: TypeAlias = List[UserMarketplacePurchase]
