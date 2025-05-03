

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CheckRunListAnnotationsResponse", "CheckRunListAnnotationsResponseItem"]


class CheckRunListAnnotationsResponseItem(BaseModel):
    annotation_level: Optional[str] = None

    blob_href: str

    end_column: Optional[int] = None

    end_line: int

    message: Optional[str] = None

    path: str

    raw_details: Optional[str] = None

    start_column: Optional[int] = None

    start_line: int

    title: Optional[str] = None


CheckRunListAnnotationsResponse: TypeAlias = List[CheckRunListAnnotationsResponseItem]
