

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .code_scanning_analysis_tool import CodeScanningAnalysisTool

__all__ = ["CodeScanningAnalysis"]


class CodeScanningAnalysis(BaseModel):
    id: int
    """Unique identifier for this analysis."""

    analysis_key: str
    """Identifies the configuration under which the analysis was executed.

    For example, in GitHub Actions this includes the workflow filename and job name.
    """

    commit_sha: str
    """The SHA of the commit to which the analysis you are uploading relates."""

    created_at: datetime
    """
    The time that the analysis was created in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    deletable: bool

    environment: str
    """
    Identifies the variable values associated with the environment in which this
    analysis was performed.
    """

    error: str

    ref: str
    """
    The Git reference, formatted as `refs/pull/<number>/merge`,
    `refs/pull/<number>/head`, `refs/heads/<branch name>` or simply `<branch name>`.
    """

    results_count: int
    """The total number of results in the analysis."""

    rules_count: int
    """The total number of rules used in the analysis."""

    sarif_id: str
    """An identifier for the upload."""

    tool: CodeScanningAnalysisTool

    url: str
    """The REST API URL of the analysis resource."""

    warning: str
    """Warning generated when processing the analysis"""

    category: Optional[str] = None
    """Identifies the configuration under which the analysis was executed.

    Used to distinguish between multiple analyses for the same tool and commit, but
    performed on different languages or different parts of the code.
    """
