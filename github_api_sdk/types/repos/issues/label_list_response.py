

from typing import List
from typing_extensions import TypeAlias

from ..label import Label

__all__ = ["LabelListResponse"]

LabelListResponse: TypeAlias = List[Label]
