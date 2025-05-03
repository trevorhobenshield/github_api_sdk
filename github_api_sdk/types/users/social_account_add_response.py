

from typing import List
from typing_extensions import TypeAlias

from .social_account import SocialAccount

__all__ = ["SocialAccountAddResponse"]

SocialAccountAddResponse: TypeAlias = List[SocialAccount]
