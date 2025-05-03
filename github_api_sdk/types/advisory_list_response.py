

from typing import List
from typing_extensions import TypeAlias

from .global_advisory import GlobalAdvisory

__all__ = ["AdvisoryListResponse"]

AdvisoryListResponse: TypeAlias = List[GlobalAdvisory]
