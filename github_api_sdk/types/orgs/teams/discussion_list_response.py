

from typing import List
from typing_extensions import TypeAlias

from .team_discussion import TeamDiscussion

__all__ = ["DiscussionListResponse"]

DiscussionListResponse: TypeAlias = List[TeamDiscussion]
