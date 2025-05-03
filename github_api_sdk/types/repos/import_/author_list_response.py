

from typing import List
from typing_extensions import TypeAlias

from .porter_author import PorterAuthor

__all__ = ["AuthorListResponse"]

AuthorListResponse: TypeAlias = List[PorterAuthor]
