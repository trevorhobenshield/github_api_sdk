

from typing import Optional

from ..._models import BaseModel

__all__ = ["NullableLicenseSimple"]


class NullableLicenseSimple(BaseModel):
    key: str

    name: str

    node_id: str

    spdx_id: Optional[str] = None

    url: Optional[str] = None

    html_url: Optional[str] = None
