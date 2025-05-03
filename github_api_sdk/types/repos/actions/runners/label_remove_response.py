

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["LabelRemoveResponse", "Label"]


class Label(BaseModel):
    name: str
    """Name of the label."""

    id: Optional[int] = None
    """Unique identifier of the label."""

    type: Optional[Literal["read-only", "custom"]] = None
    """The type of label.

    Read-only labels are applied automatically when the runner is configured.
    """


class LabelRemoveResponse(BaseModel):
    labels: List[Label]

    total_count: int
