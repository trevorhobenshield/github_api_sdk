

from typing import List
from typing_extensions import TypeAlias

from .configuration_item import ConfigurationItem

__all__ = ["DefaultListResponse"]

DefaultListResponse: TypeAlias = List[ConfigurationItem]
