

from typing import Optional

from ...._models import BaseModel

__all__ = ["CodeScanningAnalysisTool"]


class CodeScanningAnalysisTool(BaseModel):
    guid: Optional[str] = None
    """
    The GUID of the tool used to generate the code scanning analysis, if provided in
    the uploaded SARIF data.
    """

    name: Optional[str] = None
    """The name of the tool used to generate the code scanning analysis."""

    version: Optional[str] = None
    """The version of the tool used to generate the code scanning analysis."""
