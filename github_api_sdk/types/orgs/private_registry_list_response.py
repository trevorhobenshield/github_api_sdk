

from typing import List

from ..._models import BaseModel
from .org_private_registry_configuration import OrgPrivateRegistryConfiguration

__all__ = ["PrivateRegistryListResponse"]


class PrivateRegistryListResponse(BaseModel):
    configurations: List[OrgPrivateRegistryConfiguration]

    total_count: int
