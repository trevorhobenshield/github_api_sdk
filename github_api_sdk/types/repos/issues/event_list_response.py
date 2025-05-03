

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel
from ...integration import Integration
from ...orgs.simple_user import SimpleUser
from .locked_issue_event import LockedIssueEvent
from .labeled_issue_event import LabeledIssueEvent
from .renamed_issue_event import RenamedIssueEvent
from ..nullable_integration import NullableIntegration
from .unlabeled_issue_event import UnlabeledIssueEvent
from .milestoned_issue_event import MilestonedIssueEvent
from .demilestoned_issue_event import DemilestonedIssueEvent
from .added_to_project_issue_event import AddedToProjectIssueEvent
from .review_dismissed_issue_event import ReviewDismissedIssueEvent
from .review_requested_issue_event import ReviewRequestedIssueEvent
from .removed_from_project_issue_event import RemovedFromProjectIssueEvent
from .review_request_removed_issue_event import ReviewRequestRemovedIssueEvent
from .converted_note_to_issue_issue_event import ConvertedNoteToIssueIssueEvent
from .moved_column_in_project_issue_event import MovedColumnInProjectIssueEvent

__all__ = [
    "EventListResponse",
    "EventListResponseItem",
    "EventListResponseItemAssignedIssueEvent",
    "EventListResponseItemUnassignedIssueEvent",
]


class EventListResponseItemAssignedIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    assignee: SimpleUser
    """A GitHub user."""

    assigner: SimpleUser
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: str

    event: str

    node_id: str

    performed_via_github_app: Optional[Integration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    url: str


class EventListResponseItemUnassignedIssueEvent(BaseModel):
    id: int

    actor: SimpleUser
    """A GitHub user."""

    assignee: SimpleUser
    """A GitHub user."""

    assigner: SimpleUser
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


EventListResponseItem: TypeAlias = Union[
    LabeledIssueEvent,
    UnlabeledIssueEvent,
    EventListResponseItemAssignedIssueEvent,
    EventListResponseItemUnassignedIssueEvent,
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
]

EventListResponse: TypeAlias = List[EventListResponseItem]
