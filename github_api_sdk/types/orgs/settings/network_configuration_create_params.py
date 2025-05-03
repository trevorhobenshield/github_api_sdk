

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NetworkConfigurationCreateParams"]


class NetworkConfigurationCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the network configuration.

    Must be between 1 and 100 characters and may only contain upper and lowercase
    letters a-z, numbers 0-9, '.', '-', and '\\__'.
    """

    network_settings_ids: Required[list[str]]
    """The identifier of the network settings to use for the network configuration.

    Exactly one network settings must be specified.
    """

    compute_service: Literal["none", "actions"]
    """The hosted compute service to use for the network configuration."""
