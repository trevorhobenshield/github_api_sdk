

from typing import List
from typing_extensions import TypeAlias

from ..gist_simple import GistSimple

__all__ = ["ForkListResponse"]

ForkListResponse: TypeAlias = List[GistSimple]
