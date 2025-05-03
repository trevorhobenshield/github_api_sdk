

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel
from .simple_repository import SimpleRepository
from ....orgs.simple_user import SimpleUser
from .code_scanning_variant_analysis_status import CodeScanningVariantAnalysisStatus
from .code_scanning_variant_analysis_language import CodeScanningVariantAnalysisLanguage
from .code_scanning_variant_analysis_repository import CodeScanningVariantAnalysisRepository
from .code_scanning_variant_analysis_skipped_repo_group import CodeScanningVariantAnalysisSkippedRepoGroup

__all__ = [
    "CodeScanningVariantAnalysis",
    "ScannedRepository",
    "SkippedRepositories",
    "SkippedRepositoriesNotFoundRepos",
]


class ScannedRepository(BaseModel):
    analysis_status: CodeScanningVariantAnalysisStatus
    """The new status of the CodeQL variant analysis repository task."""

    repository: CodeScanningVariantAnalysisRepository
    """Repository Identifier"""

    artifact_size_in_bytes: Optional[int] = None
    """The size of the artifact. This is only available for successful analyses."""

    failure_message: Optional[str] = None
    """The reason of the failure of this repo task.

    This is only available if the repository task has failed.
    """

    result_count: Optional[int] = None
    """The number of results in the case of a successful analysis.

    This is only available for successful analyses.
    """


class SkippedRepositoriesNotFoundRepos(BaseModel):
    repository_count: int
    """The total number of repositories that were skipped for this reason."""

    repository_full_names: List[str]
    """A list of full repository names that were skipped.

    This list may not include all repositories that were skipped.
    """


class SkippedRepositories(BaseModel):
    access_mismatch_repos: CodeScanningVariantAnalysisSkippedRepoGroup

    no_codeql_db_repos: CodeScanningVariantAnalysisSkippedRepoGroup

    not_found_repos: SkippedRepositoriesNotFoundRepos

    over_limit_repos: CodeScanningVariantAnalysisSkippedRepoGroup


class CodeScanningVariantAnalysis(BaseModel):
    id: int
    """The ID of the variant analysis."""

    actor: SimpleUser
    """A GitHub user."""

    controller_repo: SimpleRepository
    """A GitHub repository."""

    query_language: CodeScanningVariantAnalysisLanguage
    """The language targeted by the CodeQL query"""

    query_pack_url: str
    """The download url for the query pack."""

    status: Literal["in_progress", "succeeded", "failed", "cancelled"]

    actions_workflow_run_id: Optional[int] = None
    """The GitHub Actions workflow run used to execute this variant analysis.

    This is only available if the workflow run has started.
    """

    completed_at: Optional[datetime] = None
    """
    The date and time at which the variant analysis was completed, in ISO 8601
    format':' YYYY-MM-DDTHH:MM:SSZ. Will be null if the variant analysis has not yet
    completed or this information is not available.
    """

    created_at: Optional[datetime] = None
    """
    The date and time at which the variant analysis was created, in ISO 8601
    format':' YYYY-MM-DDTHH:MM:SSZ.
    """

    failure_reason: Optional[Literal["no_repos_queried", "actions_workflow_run_failed", "internal_error"]] = None
    """The reason for a failure of the variant analysis.

    This is only available if the variant analysis has failed.
    """

    scanned_repositories: Optional[List[ScannedRepository]] = None

    skipped_repositories: Optional[SkippedRepositories] = None
    """Information about repositories that were skipped from processing.

    This information is only available to the user that initiated the variant
    analysis.
    """

    updated_at: Optional[datetime] = None
    """
    The date and time at which the variant analysis was last updated, in ISO 8601
    format':' YYYY-MM-DDTHH:MM:SSZ.
    """
