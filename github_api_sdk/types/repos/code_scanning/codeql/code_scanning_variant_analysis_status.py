

from typing_extensions import Literal, TypeAlias

__all__ = ["CodeScanningVariantAnalysisStatus"]

CodeScanningVariantAnalysisStatus: TypeAlias = Literal[
    "pending", "in_progress", "succeeded", "failed", "canceled", "timed_out"
]
