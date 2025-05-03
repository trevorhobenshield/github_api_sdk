

from typing import List, Optional
from typing_extensions import TypeAlias

from .....integration import Integration

__all__ = ["AppAddResponse"]

AppAddResponse: TypeAlias = List[Optional[Integration]]
