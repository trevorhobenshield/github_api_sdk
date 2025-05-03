

from typing import List, Optional
from datetime import datetime

from .actor import Actor
from .._models import BaseModel
from .repos.issue import Issue
from .repos.issues.issue_comment import IssueComment

__all__ = ["Event", "Payload", "PayloadPage", "Repo"]


class PayloadPage(BaseModel):
    action: Optional[str] = None

    html_url: Optional[str] = None

    page_name: Optional[str] = None

    sha: Optional[str] = None

    summary: Optional[str] = None

    title: Optional[str] = None


class Payload(BaseModel):
    action: Optional[str] = None

    comment: Optional[IssueComment] = None
    """Comments provide a way for people to collaborate on an issue."""

    issue: Optional[Issue] = None
    """
    Issues are a great way to keep track of tasks, enhancements, and bugs for your
    projects.
    """

    pages: Optional[List[PayloadPage]] = None


class Repo(BaseModel):
    id: int

    name: str

    url: str


class Event(BaseModel):
    id: str

    actor: Actor
    """Actor"""

    created_at: Optional[datetime] = None

    payload: Payload

    public: bool

    repo: Repo

    type: Optional[str] = None

    org: Optional[Actor] = None
    """Actor"""
