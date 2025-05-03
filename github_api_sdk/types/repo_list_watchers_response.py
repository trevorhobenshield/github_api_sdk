

from typing import List
from typing_extensions import TypeAlias

from .orgs.simple_user import SimpleUser

__all__ = ["RepoListWatchersResponse"]

RepoListWatchersResponse: TypeAlias = List[SimpleUser]
