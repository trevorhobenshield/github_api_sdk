

from typing import List, Optional

from ...._models import BaseModel
from .protection.branch_restriction_policy import BranchRestrictionPolicy
from .protection.protected_branch_admin_enforced import ProtectedBranchAdminEnforced
from .protection.protected_branch_pull_request_review import ProtectedBranchPullRequestReview

__all__ = [
    "BranchProtection",
    "AllowDeletions",
    "AllowForcePushes",
    "AllowForkSyncing",
    "BlockCreations",
    "LockBranch",
    "RequiredConversationResolution",
    "RequiredLinearHistory",
    "RequiredSignatures",
    "RequiredStatusChecks",
    "RequiredStatusChecksCheck",
]


class AllowDeletions(BaseModel):
    enabled: Optional[bool] = None


class AllowForcePushes(BaseModel):
    enabled: Optional[bool] = None


class AllowForkSyncing(BaseModel):
    enabled: Optional[bool] = None


class BlockCreations(BaseModel):
    enabled: Optional[bool] = None


class LockBranch(BaseModel):
    enabled: Optional[bool] = None


class RequiredConversationResolution(BaseModel):
    enabled: Optional[bool] = None


class RequiredLinearHistory(BaseModel):
    enabled: Optional[bool] = None


class RequiredSignatures(BaseModel):
    enabled: bool

    url: str


class RequiredStatusChecksCheck(BaseModel):
    app_id: Optional[int] = None

    context: str


class RequiredStatusChecks(BaseModel):
    checks: List[RequiredStatusChecksCheck]

    contexts: List[str]

    contexts_url: Optional[str] = None

    enforcement_level: Optional[str] = None

    strict: Optional[bool] = None

    url: Optional[str] = None


class BranchProtection(BaseModel):
    allow_deletions: Optional[AllowDeletions] = None

    allow_force_pushes: Optional[AllowForcePushes] = None

    allow_fork_syncing: Optional[AllowForkSyncing] = None
    """Whether users can pull changes from upstream when the branch is locked.

    Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    """

    block_creations: Optional[BlockCreations] = None

    enabled: Optional[bool] = None

    enforce_admins: Optional[ProtectedBranchAdminEnforced] = None
    """Protected Branch Admin Enforced"""

    lock_branch: Optional[LockBranch] = None
    """Whether to set the branch as read-only.

    If this is true, users will not be able to push to the branch.
    """

    name: Optional[str] = None

    protection_url: Optional[str] = None

    required_conversation_resolution: Optional[RequiredConversationResolution] = None

    required_linear_history: Optional[RequiredLinearHistory] = None

    required_pull_request_reviews: Optional[ProtectedBranchPullRequestReview] = None
    """Protected Branch Pull Request Review"""

    required_signatures: Optional[RequiredSignatures] = None

    required_status_checks: Optional[RequiredStatusChecks] = None
    """Protected Branch Required Status Check"""

    restrictions: Optional[BranchRestrictionPolicy] = None
    """Branch Restriction Policy"""

    url: Optional[str] = None
