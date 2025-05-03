

from typing import List
from typing_extensions import TypeAlias

from .simple_classroom_assignment import SimpleClassroomAssignment

__all__ = ["ClassroomListAssignmentsResponse"]

ClassroomListAssignmentsResponse: TypeAlias = List[SimpleClassroomAssignment]
