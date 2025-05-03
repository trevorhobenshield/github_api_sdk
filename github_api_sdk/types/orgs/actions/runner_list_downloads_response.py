

from typing import List
from typing_extensions import TypeAlias

from .application import Application

__all__ = ["RunnerListDownloadsResponse"]

RunnerListDownloadsResponse: TypeAlias = List[Application]
