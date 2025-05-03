

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..issue import Issue
from ...._models import BaseModel
from ..commit_comment import CommitComment
from ...orgs.simple_user import SimpleUser
from .locked_issue_event import LockedIssueEvent
from .labeled_issue_event import LabeledIssueEvent
from .renamed_issue_event import RenamedIssueEvent
from ..nullable_integration import NullableIntegration
from .unlabeled_issue_event import UnlabeledIssueEvent
from .milestoned_issue_event import MilestonedIssueEvent
from .demilestoned_issue_event import DemilestonedIssueEvent
from ...gists.author_association import AuthorAssociation
from ...orgs.teams.reaction_rollup import ReactionRollup
from .added_to_project_issue_event import AddedToProjectIssueEvent
from .review_dismissed_issue_event import ReviewDismissedIssueEvent
from .review_requested_issue_event import ReviewRequestedIssueEvent
from .removed_from_project_issue_event import RemovedFromProjectIssueEvent
from ..pulls.pull_request_review_comment import PullRequestReviewComment
from .review_request_removed_issue_event import ReviewRequestRemovedIssueEvent
from .converted_note_to_issue_issue_event import ConvertedNoteToIssueIssueEvent
from .moved_column_in_project_issue_event import MovedColumnInProjectIssueEvent

__all__ = [
    "TimelineListResponse",
    "TimelineListResponseItem",
    "TimelineListResponseItemTimelineCommentEvent",
    "TimelineListResponseItemTimelineCrossReferencedEvent",
    "TimelineListResponseItemTimelineCrossReferencedEventSource",
    "TimelineListResponseItemTimelineCommittedEvent",
    "TimelineListResponseItemTimelineCommittedEventAuthor",
    "TimelineListResponseItemTimelineCommittedEventCommitter",
    "TimelineListResponseItemTimelineCommittedEventParent",
    "TimelineListResponseItemTimelineCommittedEventTree",
    "TimelineListResponseItemTimelineCommittedEventVerification",
    "TimelineListResponseItemTimelineReviewedEvent",
    "TimelineListResponseItemTimelineReviewedEvent_Links",
    "TimelineListResponseItemTimelineReviewedEvent_LinksHTML",
    "TimelineListResponseItemTimelineReviewedEvent_LinksPullRequest",
    "TimelineListResponseItemTimelineLineCommentedEvent",
    "TimelineListResponseItemTimelineCommitCommentedEvent",
    "TimelineListResponseItemTimelineAssignedIssueEvent",
    "TimelineListResponseItemTimelineUnassignedIssueEvent",
    "TimelineListResponseItemStateChangeIssueEvent",
]


class TimelineListResponseItemTimelineCommentEvent(BaseModel):
    id: int
    """Unique identifier of the issue comment"""

    actor: SimpleUser
    """A GitHub user."""

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    created_at: datetime

    event: str

    html_url: str

    issue_url: str

    node_id: str

    updated_at: datetime

    url: str
    """URL for the issue comment"""

    user: SimpleUser
    """A GitHub user."""

    body: Optional[str] = None
    """Contents of the issue comment"""

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    reactions: Optional[ReactionRollup] = None


class TimelineListResponseItemTimelineCrossReferencedEventSource(BaseModel):
    issue: Optional[Issue] = None
    """
    Issues are a great way to keep track of tasks, enhancements, and bugs for your
    projects.
    """

    type: Optional[str] = None


class TimelineListResponseItemTimelineCrossReferencedEvent(BaseModel):
    created_at: datetime

    event: str

    source: TimelineListResponseItemTimelineCrossReferencedEventSource

    updated_at: datetime

    actor: Optional[SimpleUser] = None
    """A GitHub user."""


class TimelineListResponseItemTimelineCommittedEventAuthor(BaseModel):
    date: datetime
    """Timestamp of the commit"""

    email: str
    """Git email address of the user"""

    name: str
    """Name of the git user"""


class TimelineListResponseItemTimelineCommittedEventCommitter(BaseModel):
    date: datetime
    """Timestamp of the commit"""

    email: str
    """Git email address of the user"""

    name: str
    """Name of the git user"""


class TimelineListResponseItemTimelineCommittedEventParent(BaseModel):
    html_url: str

    sha: str
    """SHA for the commit"""

    url: str


class TimelineListResponseItemTimelineCommittedEventTree(BaseModel):
    sha: str
    """SHA for the commit"""

    url: str


class TimelineListResponseItemTimelineCommittedEventVerification(BaseModel):
    payload: Optional[str] = None

    reason: str

    signature: Optional[str] = None

    verified: bool

    verified_at: Optional[str] = None


class TimelineListResponseItemTimelineCommittedEvent(BaseModel):
    author: TimelineListResponseItemTimelineCommittedEventAuthor
    """Identifying information for the git-user"""

    committer: TimelineListResponseItemTimelineCommittedEventCommitter
    """Identifying information for the git-user"""

    html_url: str

    message: str
    """Message describing the purpose of the commit"""

    node_id: str

    parents: List[TimelineListResponseItemTimelineCommittedEventParent]

    sha: str
    """SHA for the commit"""

    tree: TimelineListResponseItemTimelineCommittedEventTree

    url: str

    verification: TimelineListResponseItemTimelineCommittedEventVerification

    event: Optional[str] = None


class TimelineListResponseItemTimelineReviewedEvent_LinksHTML(BaseModel):
    href: str


class TimelineListResponseItemTimelineReviewedEvent_LinksPullRequest(BaseModel):
    href: str


class TimelineListResponseItemTimelineReviewedEvent_Links(BaseModel):
    html: TimelineListResponseItemTimelineReviewedEvent_LinksHTML

    pull_request: TimelineListResponseItemTimelineReviewedEvent_LinksPullRequest


class TimelineListResponseItemTimelineReviewedEvent(BaseModel):
    id: int
    """Unique identifier of the review"""

    api_links: TimelineListResponseItemTimelineReviewedEvent_Links = FieldInfo(alias="_links")

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    body: Optional[str] = None
    """The text of the review."""

    commit_id: str
    """A commit SHA for the review."""

    event: str

    html_url: str

    node_id: str

    pull_request_url: str

    state: str

    user: SimpleUser
    """A GitHub user."""

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    submitted_at: Optional[datetime] = None


class TimelineListResponseItemTimelineLineCommentedEvent(BaseModel):
    comments: Optional[List[PullRequestReviewComment]] = None

    event: Optional[str] = None

    node_id: Optional[str] = None


class TimelineListResponseItemTimelineCommitCommentedEvent(BaseModel):
    comments: Optional[List[CommitComment]] = None

    commit_id: Optional[str] = None

    event: Optional[str] = None

    node_id: Optional[str] = None


class TimelineListResponseItemTimelineAssignedIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    assignee: SimpleUser
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: str

    event: str

    node_id: str

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    url: str


class TimelineListResponseItemTimelineUnassignedIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    assignee: SimpleUser
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: str

    event: str

    node_id: str

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    url: str


class TimelineListResponseItemStateChangeIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: str

    event: str

    node_id: str

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    url: str

    state_reason: Optional[str] = None


TimelineListResponseItem: TypeAlias = Union[
    LabeledIssueEvent,
    UnlabeledIssueEvent,
    MilestonedIssueEvent,
    DemilestonedIssueEvent,
    RenamedIssueEvent,
    ReviewRequestedIssueEvent,
    ReviewRequestRemovedIssueEvent,
    ReviewDismissedIssueEvent,
    LockedIssueEvent,
    AddedToProjectIssueEvent,
    MovedColumnInProjectIssueEvent,
    RemovedFromProjectIssueEvent,
    ConvertedNoteToIssueIssueEvent,
    TimelineListResponseItemTimelineCommentEvent,
    TimelineListResponseItemTimelineCrossReferencedEvent,
    TimelineListResponseItemTimelineCommittedEvent,
    TimelineListResponseItemTimelineReviewedEvent,
    TimelineListResponseItemTimelineLineCommentedEvent,
    TimelineListResponseItemTimelineCommitCommentedEvent,
    TimelineListResponseItemTimelineAssignedIssueEvent,
    TimelineListResponseItemTimelineUnassignedIssueEvent,
    TimelineListResponseItemStateChangeIssueEvent,
]

TimelineListResponse: TypeAlias = List[TimelineListResponseItem]
