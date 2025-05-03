

from typing import List
from typing_extensions import TypeAlias

from ..enterprises.organization_alert import OrganizationAlert

__all__ = ["SecretScanningListAlertsResponse"]

SecretScanningListAlertsResponse: TypeAlias = List[OrganizationAlert]
