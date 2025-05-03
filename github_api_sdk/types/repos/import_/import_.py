

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Import", "ProjectChoice"]


class ProjectChoice(BaseModel):
    human_name: Optional[str] = None

    tfvc_project: Optional[str] = None

    vcs: Optional[str] = None


class Import(BaseModel):
    authors_url: str

    html_url: str

    repository_url: str

    status: Literal[
        "auth",
        "error",
        "none",
        "detecting",
        "choose",
        "auth_failed",
        "importing",
        "mapping",
        "waiting_to_push",
        "pushing",
        "complete",
        "setup",
        "unknown",
        "detection_found_multiple",
        "detection_found_nothing",
        "detection_needs_auth",
    ]

    url: str

    vcs: Optional[str] = None

    vcs_url: str
    """The URL of the originating repository."""

    authors_count: Optional[int] = None

    commit_count: Optional[int] = None

    error_message: Optional[str] = None

    failed_step: Optional[str] = None

    has_large_files: Optional[bool] = None

    import_percent: Optional[int] = None

    large_files_count: Optional[int] = None

    large_files_size: Optional[int] = None

    message: Optional[str] = None

    project_choices: Optional[List[ProjectChoice]] = None

    push_percent: Optional[int] = None

    status_text: Optional[str] = None

    svc_root: Optional[str] = None

    svn_root: Optional[str] = None

    tfvc_project: Optional[str] = None

    use_lfs: Optional[bool] = None
