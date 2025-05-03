

from typing import List
from typing_extensions import TypeAlias

from .comments.reaction import Reaction

__all__ = ["ReactionListResponse"]

ReactionListResponse: TypeAlias = List[Reaction]
