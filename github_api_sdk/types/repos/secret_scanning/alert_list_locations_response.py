

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "AlertListLocationsResponse",
    "AlertListLocationsResponseItem",
    "AlertListLocationsResponseItemDetails",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationCommit",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationWikiCommit",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationIssueTitle",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationIssueBody",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationIssueComment",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionTitle",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionBody",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionComment",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestTitle",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestBody",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestComment",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestReview",
    "AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestReviewComment",
]


class AlertListLocationsResponseItemDetailsSecretScanningLocationCommit(BaseModel):
    blob_sha: str
    """SHA-1 hash ID of the associated blob"""

    blob_url: str
    """The API URL to get the associated blob resource"""

    commit_sha: str
    """SHA-1 hash ID of the associated commit"""

    commit_url: str
    """The API URL to get the associated commit resource"""

    end_column: float
    """
    The column at which the secret ends within the end line when the file is
    interpreted as 8BIT ASCII
    """

    end_line: float
    """Line number at which the secret ends in the file"""

    path: str
    """The file path in the repository"""

    start_column: float
    """
    The column at which the secret starts within the start line when the file is
    interpreted as 8BIT ASCII
    """

    start_line: float
    """Line number at which the secret starts in the file"""


class AlertListLocationsResponseItemDetailsSecretScanningLocationWikiCommit(BaseModel):
    blob_sha: str
    """SHA-1 hash ID of the associated blob"""

    commit_sha: str
    """SHA-1 hash ID of the associated commit"""

    commit_url: str
    """The GitHub URL to get the associated wiki commit"""

    end_column: float
    """
    The column at which the secret ends within the end line when the file is
    interpreted as 8-bit ASCII.
    """

    end_line: float
    """Line number at which the secret ends in the file"""

    page_url: str
    """The GitHub URL to get the associated wiki page"""

    path: str
    """The file path of the wiki page"""

    start_column: float
    """
    The column at which the secret starts within the start line when the file is
    interpreted as 8-bit ASCII.
    """

    start_line: float
    """Line number at which the secret starts in the file"""


class AlertListLocationsResponseItemDetailsSecretScanningLocationIssueTitle(BaseModel):
    issue_title_url: str
    """The API URL to get the issue where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationIssueBody(BaseModel):
    issue_body_url: str
    """The API URL to get the issue where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationIssueComment(BaseModel):
    issue_comment_url: str
    """The API URL to get the issue comment where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionTitle(BaseModel):
    discussion_title_url: str
    """The URL to the discussion where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionBody(BaseModel):
    discussion_body_url: str
    """The URL to the discussion where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionComment(BaseModel):
    discussion_comment_url: str
    """The API URL to get the discussion comment where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestTitle(BaseModel):
    pull_request_title_url: str
    """The API URL to get the pull request where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestBody(BaseModel):
    pull_request_body_url: str
    """The API URL to get the pull request where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestComment(BaseModel):
    pull_request_comment_url: str
    """The API URL to get the pull request comment where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestReview(BaseModel):
    pull_request_review_url: str
    """The API URL to get the pull request review where the secret was detected."""


class AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestReviewComment(BaseModel):
    pull_request_review_comment_url: str
    """
    The API URL to get the pull request review comment where the secret was
    detected.
    """


AlertListLocationsResponseItemDetails: TypeAlias = Union[
    AlertListLocationsResponseItemDetailsSecretScanningLocationCommit,
    AlertListLocationsResponseItemDetailsSecretScanningLocationWikiCommit,
    AlertListLocationsResponseItemDetailsSecretScanningLocationIssueTitle,
    AlertListLocationsResponseItemDetailsSecretScanningLocationIssueBody,
    AlertListLocationsResponseItemDetailsSecretScanningLocationIssueComment,
    AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionTitle,
    AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionBody,
    AlertListLocationsResponseItemDetailsSecretScanningLocationDiscussionComment,
    AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestTitle,
    AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestBody,
    AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestComment,
    AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestReview,
    AlertListLocationsResponseItemDetailsSecretScanningLocationPullRequestReviewComment,
]


class AlertListLocationsResponseItem(BaseModel):
    details: Optional[AlertListLocationsResponseItemDetails] = None
    """Represents a 'commit' secret scanning location type.

    This location type shows that a secret was detected inside a commit to a
    repository.
    """

    type: Optional[
        Literal[
            "commit",
            "wiki_commit",
            "issue_title",
            "issue_body",
            "issue_comment",
            "discussion_title",
            "discussion_body",
            "discussion_comment",
            "pull_request_title",
            "pull_request_body",
            "pull_request_comment",
            "pull_request_review",
            "pull_request_review_comment",
        ]
    ] = None
    """The location type.

    Because secrets may be found in different types of resources (ie. code,
    comments, issues, pull requests, discussions), this field identifies the type of
    resource where the secret was found.
    """


AlertListLocationsResponse: TypeAlias = List[AlertListLocationsResponseItem]
