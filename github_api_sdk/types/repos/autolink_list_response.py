

from typing import List
from typing_extensions import TypeAlias

from .autolink import Autolink

__all__ = ["AutolinkListResponse"]

AutolinkListResponse: TypeAlias = List[Autolink]
