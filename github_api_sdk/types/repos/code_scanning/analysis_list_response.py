

from typing import List
from typing_extensions import TypeAlias

from .code_scanning_analysis import CodeScanningAnalysis

__all__ = ["AnalysisListResponse"]

AnalysisListResponse: TypeAlias = List[CodeScanningAnalysis]
