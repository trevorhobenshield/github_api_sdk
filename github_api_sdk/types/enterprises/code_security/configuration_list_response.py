

from typing import List
from typing_extensions import TypeAlias

from .configuration import Configuration

__all__ = ["ConfigurationListResponse"]

ConfigurationListResponse: TypeAlias = List[Configuration]
