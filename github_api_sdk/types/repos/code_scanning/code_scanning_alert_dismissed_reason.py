

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["CodeScanningAlertDismissedReason"]

CodeScanningAlertDismissedReason: TypeAlias = Optional[Literal["false positive", "won't fix", "used in tests"]]
