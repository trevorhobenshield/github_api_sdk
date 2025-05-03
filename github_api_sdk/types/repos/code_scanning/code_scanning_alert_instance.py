

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .code_scanning_alert_state import CodeScanningAlertState

__all__ = ["CodeScanningAlertInstance", "Location", "Message"]


class Location(BaseModel):
    end_column: Optional[int] = None

    end_line: Optional[int] = None

    path: Optional[str] = None

    start_column: Optional[int] = None

    start_line: Optional[int] = None


class Message(BaseModel):
    text: Optional[str] = None


class CodeScanningAlertInstance(BaseModel):
    analysis_key: Optional[str] = None
    """Identifies the configuration under which the analysis was executed.

    For example, in GitHub Actions this includes the workflow filename and job name.
    """

    category: Optional[str] = None
    """Identifies the configuration under which the analysis was executed.

    Used to distinguish between multiple analyses for the same tool and commit, but
    performed on different languages or different parts of the code.
    """

    classifications: Optional[List[Optional[Literal["source", "generated", "test", "library"]]]] = None
    """
    Classifications that have been applied to the file that triggered the alert. For
    example identifying it as documentation, or a generated file.
    """

    commit_sha: Optional[str] = None

    environment: Optional[str] = None
    """
    Identifies the variable values associated with the environment in which the
    analysis that generated this alert instance was performed, such as the language
    that was analyzed.
    """

    html_url: Optional[str] = None

    location: Optional[Location] = None
    """Describe a region within a file for the alert."""

    message: Optional[Message] = None

    ref: Optional[str] = None
    """
    The Git reference, formatted as `refs/pull/<number>/merge`,
    `refs/pull/<number>/head`, `refs/heads/<branch name>` or simply `<branch name>`.
    """

    state: Optional[CodeScanningAlertState] = None
    """State of a code scanning alert."""
