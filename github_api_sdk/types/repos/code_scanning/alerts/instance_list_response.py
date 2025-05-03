

from typing import List
from typing_extensions import TypeAlias

from ..code_scanning_alert_instance import CodeScanningAlertInstance

__all__ = ["InstanceListResponse"]

InstanceListResponse: TypeAlias = List[CodeScanningAlertInstance]
