

from typing import List
from typing_extensions import TypeAlias

from .deploy_key import DeployKey

__all__ = ["KeyListResponse"]

KeyListResponse: TypeAlias = List[DeployKey]
