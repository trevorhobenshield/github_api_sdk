

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["LicenseListResponse", "LicenseListResponseItem"]


class LicenseListResponseItem(BaseModel):
    key: str

    name: str

    node_id: str

    spdx_id: Optional[str] = None

    url: Optional[str] = None

    html_url: Optional[str] = None


LicenseListResponse: TypeAlias = List[LicenseListResponseItem]
