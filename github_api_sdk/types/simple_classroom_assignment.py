

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .simple_classroom import SimpleClassroom

__all__ = ["SimpleClassroomAssignment"]


class SimpleClassroomAssignment(BaseModel):
    id: int
    """Unique identifier of the repository."""

    accepted: int
    """The number of students that have accepted the assignment."""

    classroom: SimpleClassroom
    """A GitHub Classroom classroom"""

    deadline: Optional[datetime] = None
    """The time at which the assignment is due."""

    editor: str
    """The selected editor for the assignment."""

    feedback_pull_requests_enabled: bool
    """Whether feedback pull request will be created on assignment acceptance."""

    invitations_enabled: bool
    """Whether the invitation link is enabled.

    Visiting an enabled invitation link will accept the assignment.
    """

    invite_link: str
    """The link that a student can use to accept the assignment."""

    language: str
    """The programming language used in the assignment."""

    passing: int
    """The number of students that have passed the assignment."""

    public_repo: bool
    """Whether an accepted assignment creates a public repository."""

    slug: str
    """Sluggified name of the assignment."""

    students_are_repo_admins: bool
    """Whether students are admins on created repository on accepted assignment."""

    submitted: int
    """The number of students that have submitted the assignment."""

    title: str
    """Assignment title."""

    type: Literal["individual", "group"]
    """Whether it's a Group Assignment or Individual Assignment."""

    max_members: Optional[int] = None
    """The maximum allowable members per team."""

    max_teams: Optional[int] = None
    """The maximum allowable teams for the assignment."""
