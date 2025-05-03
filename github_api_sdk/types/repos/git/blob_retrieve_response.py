

from typing import Optional

from ...._models import BaseModel

__all__ = ["BlobRetrieveResponse"]


class BlobRetrieveResponse(BaseModel):
    content: str

    encoding: str

    node_id: str

    sha: str

    size: Optional[int] = None

    url: str

    highlighted_content: Optional[str] = None
