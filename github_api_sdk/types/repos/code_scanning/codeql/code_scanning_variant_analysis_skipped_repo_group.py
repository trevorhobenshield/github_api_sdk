

from typing import List

from ....._models import BaseModel
from .code_scanning_variant_analysis_repository import CodeScanningVariantAnalysisRepository

__all__ = ["CodeScanningVariantAnalysisSkippedRepoGroup"]


class CodeScanningVariantAnalysisSkippedRepoGroup(BaseModel):
    repositories: List[CodeScanningVariantAnalysisRepository]
    """A list of repositories that were skipped.

    This list may not include all repositories that were skipped. This is only
    available when the repository was found and the user has access to it.
    """

    repository_count: int
    """The total number of repositories that were skipped for this reason."""
