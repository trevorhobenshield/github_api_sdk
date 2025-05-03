

from typing_extensions import Literal

from ..._models import BaseModel
from ..orgs.simple_user import SimpleUser

__all__ = ["AutoMerge"]


class AutoMerge(BaseModel):
    commit_message: str
    """Commit message for the merge commit."""

    commit_title: str
    """Title for the merge commit message."""

    enabled_by: SimpleUser
    """A GitHub user."""

    merge_method: Literal["merge", "squash", "rebase"]
    """The merge method to use."""
