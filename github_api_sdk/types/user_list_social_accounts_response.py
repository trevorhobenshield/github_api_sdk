

from typing import List
from typing_extensions import TypeAlias

from .users.social_account import SocialAccount

__all__ = ["UserListSocialAccountsResponse"]

UserListSocialAccountsResponse: TypeAlias = List[SocialAccount]
