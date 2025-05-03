

from typing import List
from typing_extensions import TypeAlias

from .project_card import ProjectCard

__all__ = ["CardListResponse"]

CardListResponse: TypeAlias = List[ProjectCard]
