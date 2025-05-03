

from typing import List
from typing_extensions import TypeAlias

from ...marketplace_purchase import MarketplacePurchase

__all__ = ["AccountListResponse"]

AccountListResponse: TypeAlias = List[MarketplacePurchase]
