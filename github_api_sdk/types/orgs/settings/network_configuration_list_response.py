

from typing import List

from ...._models import BaseModel
from .network_configuration import NetworkConfiguration

__all__ = ["NetworkConfigurationListResponse"]


class NetworkConfigurationListResponse(BaseModel):
    network_configurations: List[NetworkConfiguration]

    total_count: int
