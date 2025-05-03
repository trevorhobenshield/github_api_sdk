

from typing import List
from typing_extensions import TypeAlias

from .gists.base_gist import BaseGist

__all__ = ["GistListStarredResponse"]

GistListStarredResponse: TypeAlias = List[BaseGist]
