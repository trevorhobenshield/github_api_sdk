

from typing import List
from typing_extensions import TypeAlias

from ...enterprises.code_security.repositories import Repositories

__all__ = ["ConfigurationListRepositoriesResponse"]

ConfigurationListRepositoriesResponse: TypeAlias = List[Repositories]
