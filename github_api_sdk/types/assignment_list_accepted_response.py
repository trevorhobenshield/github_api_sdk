

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel
from .simple_classroom_assignment import SimpleClassroomAssignment
from .simple_classroom_repository import SimpleClassroomRepository

__all__ = [
    "AssignmentListAcceptedResponse",
    "AssignmentListAcceptedResponseItem",
    "AssignmentListAcceptedResponseItemStudent",
]


class AssignmentListAcceptedResponseItemStudent(BaseModel):
    id: int

    avatar_url: str

    html_url: str

    login: str


class AssignmentListAcceptedResponseItem(BaseModel):
    id: int
    """Unique identifier of the repository."""

    assignment: SimpleClassroomAssignment
    """A GitHub Classroom assignment"""

    commit_count: int
    """Count of student commits."""

    grade: str
    """Most recent grade."""

    passing: bool
    """Whether a submission passed."""

    repository: SimpleClassroomRepository
    """A GitHub repository view for Classroom"""

    students: List[AssignmentListAcceptedResponseItemStudent]

    submitted: bool
    """Whether an accepted assignment has been submitted."""


AssignmentListAcceptedResponse: TypeAlias = List[AssignmentListAcceptedResponseItem]
