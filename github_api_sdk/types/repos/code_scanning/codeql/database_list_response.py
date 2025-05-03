

from typing import List
from typing_extensions import TypeAlias

from .code_scanning_codeql_database import CodeScanningCodeqlDatabase

__all__ = ["DatabaseListResponse"]

DatabaseListResponse: TypeAlias = List[CodeScanningCodeqlDatabase]
