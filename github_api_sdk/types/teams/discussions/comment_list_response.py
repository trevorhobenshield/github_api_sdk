

from typing import List
from typing_extensions import TypeAlias

from ...orgs.teams.discussions.team_discussion_comment import TeamDiscussionComment

__all__ = ["CommentListResponse"]

CommentListResponse: TypeAlias = List[TeamDiscussionComment]
