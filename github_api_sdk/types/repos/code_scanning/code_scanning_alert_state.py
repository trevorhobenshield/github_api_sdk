

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["CodeScanningAlertState"]

CodeScanningAlertState: TypeAlias = Optional[Literal["open", "dismissed", "fixed"]]
