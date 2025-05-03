

from typing import List
from typing_extensions import TypeAlias

from .simple_classroom import SimpleClassroom

__all__ = ["ClassroomListResponse"]

ClassroomListResponse: TypeAlias = List[SimpleClassroom]
