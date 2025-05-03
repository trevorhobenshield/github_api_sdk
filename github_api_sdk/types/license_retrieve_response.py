

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LicenseRetrieveResponse"]


class LicenseRetrieveResponse(BaseModel):
    body: str

    conditions: List[str]

    description: str

    featured: bool

    html_url: str

    implementation: str

    key: str

    limitations: List[str]

    name: str

    node_id: str

    permissions: List[str]

    spdx_id: Optional[str] = None

    url: Optional[str] = None
