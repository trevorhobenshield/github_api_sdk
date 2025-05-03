

from typing import List, Optional

from ......_models import BaseModel

__all__ = ["SubRetrieveResponse"]


class SubRetrieveResponse(BaseModel):
    use_default: bool
    """Whether to use the default template or not.

    If `true`, the `include_claim_keys` field is ignored.
    """

    include_claim_keys: Optional[List[str]] = None
    """Array of unique strings.

    Each claim key can only contain alphanumeric characters and underscores.
    """
