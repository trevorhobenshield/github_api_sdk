

from typing import List
from typing_extensions import TypeAlias

from .organization_alert import OrganizationAlert

__all__ = ["SecretScanningListAlertsResponse"]

SecretScanningListAlertsResponse: TypeAlias = List[OrganizationAlert]
