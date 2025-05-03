

from typing import List
from typing_extensions import TypeAlias

from .milestone import Milestone

__all__ = ["MilestoneListResponse"]

MilestoneListResponse: TypeAlias = List[Milestone]
