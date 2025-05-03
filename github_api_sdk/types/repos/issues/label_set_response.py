

from typing import List
from typing_extensions import TypeAlias

from ..label import Label

__all__ = ["LabelSetResponse"]

LabelSetResponse: TypeAlias = List[Label]
