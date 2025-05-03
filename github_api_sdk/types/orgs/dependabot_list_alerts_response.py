

from typing import List
from typing_extensions import TypeAlias

from ..enterprises.alert_with_repository import AlertWithRepository

__all__ = ["DependabotListAlertsResponse"]

DependabotListAlertsResponse: TypeAlias = List[AlertWithRepository]
