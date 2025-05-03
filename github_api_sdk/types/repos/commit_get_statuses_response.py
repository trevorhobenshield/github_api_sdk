

from typing import List
from typing_extensions import TypeAlias

from ..status import Status

__all__ = ["CommitGetStatusesResponse"]

CommitGetStatusesResponse: TypeAlias = List[Status]
