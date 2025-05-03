

from typing import List, Optional

from ...._models import BaseModel
from ...orgs.team import Team
from ...integration import Integration
from ...orgs.simple_user import SimpleUser
from .protection.status_check_policy import StatusCheckPolicy
from .protection.branch_restriction_policy import BranchRestrictionPolicy

__all__ = [
    "ProtectionUpdateResponse",
    "AllowDeletions",
    "AllowForcePushes",
    "AllowForkSyncing",
    "BlockCreations",
    "EnforceAdmins",
    "LockBranch",
    "RequiredConversationResolution",
    "RequiredLinearHistory",
    "RequiredPullRequestReviews",
    "RequiredPullRequestReviewsBypassPullRequestAllowances",
    "RequiredPullRequestReviewsDismissalRestrictions",
    "RequiredSignatures",
]


class AllowDeletions(BaseModel):
    enabled: bool


class AllowForcePushes(BaseModel):
    enabled: bool


class AllowForkSyncing(BaseModel):
    enabled: Optional[bool] = None


class BlockCreations(BaseModel):
    enabled: bool


class EnforceAdmins(BaseModel):
    enabled: bool

    url: str


class LockBranch(BaseModel):
    enabled: Optional[bool] = None


class RequiredConversationResolution(BaseModel):
    enabled: Optional[bool] = None


class RequiredLinearHistory(BaseModel):
    enabled: bool


class RequiredPullRequestReviewsBypassPullRequestAllowances(BaseModel):
    teams: List[Team]

    users: List[SimpleUser]

    apps: Optional[List[Optional[Integration]]] = None


class RequiredPullRequestReviewsDismissalRestrictions(BaseModel):
    teams: List[Team]

    teams_url: str

    url: str

    users: List[SimpleUser]

    users_url: str

    apps: Optional[List[Optional[Integration]]] = None


class RequiredPullRequestReviews(BaseModel):
    url: str

    bypass_pull_request_allowances: Optional[RequiredPullRequestReviewsBypassPullRequestAllowances] = None

    dismiss_stale_reviews: Optional[bool] = None

    dismissal_restrictions: Optional[RequiredPullRequestReviewsDismissalRestrictions] = None

    require_code_owner_reviews: Optional[bool] = None

    require_last_push_approval: Optional[bool] = None
    """
    Whether the most recent push must be approved by someone other than the person
    who pushed it.
    """

    required_approving_review_count: Optional[int] = None


class RequiredSignatures(BaseModel):
    enabled: bool

    url: str


class ProtectionUpdateResponse(BaseModel):
    url: str

    allow_deletions: Optional[AllowDeletions] = None

    allow_force_pushes: Optional[AllowForcePushes] = None

    allow_fork_syncing: Optional[AllowForkSyncing] = None
    """Whether users can pull changes from upstream when the branch is locked.

    Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    """

    block_creations: Optional[BlockCreations] = None

    enforce_admins: Optional[EnforceAdmins] = None

    lock_branch: Optional[LockBranch] = None
    """Whether to set the branch as read-only.

    If this is true, users will not be able to push to the branch.
    """

    required_conversation_resolution: Optional[RequiredConversationResolution] = None

    required_linear_history: Optional[RequiredLinearHistory] = None

    required_pull_request_reviews: Optional[RequiredPullRequestReviews] = None

    required_signatures: Optional[RequiredSignatures] = None

    required_status_checks: Optional[StatusCheckPolicy] = None
    """Status Check Policy"""

    restrictions: Optional[BranchRestrictionPolicy] = None
    """Branch Restriction Policy"""
