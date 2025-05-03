

from typing import List

from ......_models import BaseModel

__all__ = ["CustomSub"]


class CustomSub(BaseModel):
    include_claim_keys: List[str]
    """Array of unique strings.

    Each claim key can only contain alphanumeric characters and underscores.
    """
