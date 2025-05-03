

from typing import List
from typing_extensions import TypeAlias

from .dependabot_alert import DependabotAlert

__all__ = ["AlertListResponse"]

AlertListResponse: TypeAlias = List[DependabotAlert]
