

from typing import List
from typing_extensions import TypeAlias

from ....enterprises.code_security.configurations.configuration_item import ConfigurationItem

__all__ = ["DefaultListResponse"]

DefaultListResponse: TypeAlias = List[ConfigurationItem]
