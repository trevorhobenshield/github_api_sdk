

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .applications.user import User

__all__ = ["RepoListActivityResponse", "RepoListActivityResponseItem"]


class RepoListActivityResponseItem(BaseModel):
    id: int

    activity_type: Literal["push", "force_push", "branch_deletion", "branch_creation", "pr_merge", "merge_queue_merge"]
    """The type of the activity that was performed."""

    actor: Optional[User] = None
    """A GitHub user."""

    after: str
    """The SHA of the commit after the activity."""

    before: str
    """The SHA of the commit before the activity."""

    node_id: str

    ref: str
    """The full Git reference, formatted as `refs/heads/<branch name>`."""

    timestamp: datetime
    """The time when the activity occurred."""


RepoListActivityResponse: TypeAlias = List[RepoListActivityResponseItem]
