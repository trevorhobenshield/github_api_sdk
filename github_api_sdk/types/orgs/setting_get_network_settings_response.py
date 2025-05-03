

from typing import Optional

from ..._models import BaseModel

__all__ = ["SettingGetNetworkSettingsResponse"]


class SettingGetNetworkSettingsResponse(BaseModel):
    id: str
    """The unique identifier of the network settings resource."""

    name: str
    """The name of the network settings resource."""

    region: str
    """The location of the subnet this network settings resource is configured for."""

    subnet_id: str
    """The subnet this network settings resource is configured for."""

    network_configuration_id: Optional[str] = None
    """
    The identifier of the network configuration that is using this settings
    resource.
    """
