

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SarifRetrieveResponse"]


class SarifRetrieveResponse(BaseModel):
    analyses_url: Optional[str] = None
    """The REST API URL for getting the analyses associated with the upload."""

    errors: Optional[List[str]] = None
    """Any errors that ocurred during processing of the delivery."""

    processing_status: Optional[Literal["pending", "complete", "failed"]] = None
    """
    `pending` files have not yet been processed, while `complete` means results from
    the SARIF have been stored. `failed` files have either not been processed at
    all, or could only be partially processed.
    """
