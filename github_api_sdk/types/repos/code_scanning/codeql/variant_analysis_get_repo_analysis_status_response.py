

from typing import Optional

from ....._models import BaseModel
from .simple_repository import SimpleRepository
from .code_scanning_variant_analysis_status import CodeScanningVariantAnalysisStatus

__all__ = ["VariantAnalysisGetRepoAnalysisStatusResponse"]


class VariantAnalysisGetRepoAnalysisStatusResponse(BaseModel):
    analysis_status: CodeScanningVariantAnalysisStatus
    """The new status of the CodeQL variant analysis repository task."""

    repository: SimpleRepository
    """A GitHub repository."""

    artifact_size_in_bytes: Optional[int] = None
    """The size of the artifact. This is only available for successful analyses."""

    artifact_url: Optional[str] = None
    """The URL of the artifact. This is only available for successful analyses."""

    database_commit_sha: Optional[str] = None
    """The SHA of the commit the CodeQL database was built against.

    This is only available for successful analyses.
    """

    failure_message: Optional[str] = None
    """The reason of the failure of this repo task.

    This is only available if the repository task has failed.
    """

    result_count: Optional[int] = None
    """The number of results in the case of a successful analysis.

    This is only available for successful analyses.
    """

    source_location_prefix: Optional[str] = None
    """The source location prefix to use.

    This is only available for successful analyses.
    """
