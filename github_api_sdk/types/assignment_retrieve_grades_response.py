

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AssignmentRetrieveGradesResponse", "AssignmentRetrieveGradesResponseItem"]


class AssignmentRetrieveGradesResponseItem(BaseModel):
    assignment_name: str
    """Name of the assignment"""

    assignment_url: str
    """URL of the assignment"""

    github_username: str
    """GitHub username of the student"""

    points_available: int
    """Number of points available for the assignment"""

    points_awarded: int
    """Number of points awarded to the student"""

    roster_identifier: str
    """Roster identifier of the student"""

    starter_code_url: str
    """URL of the starter code for the assignment"""

    student_repository_name: str
    """Name of the student's assignment repository"""

    student_repository_url: str
    """URL of the student's assignment repository"""

    submission_timestamp: str
    """Timestamp of the student's assignment submission"""

    group_name: Optional[str] = None
    """If a group assignment, name of the group the student is in"""


AssignmentRetrieveGradesResponse: TypeAlias = List[AssignmentRetrieveGradesResponseItem]
