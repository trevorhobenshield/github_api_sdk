

from typing import List
from typing_extensions import TypeAlias

from .code_of_conduct import CodeOfConduct

__all__ = ["CodesOfConductListResponse"]

CodesOfConductListResponse: TypeAlias = List[CodeOfConduct]
