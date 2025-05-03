

from typing import List
from typing_extensions import TypeAlias

from .social_account import SocialAccount

__all__ = ["SocialAccountListResponse"]

SocialAccountListResponse: TypeAlias = List[SocialAccount]
