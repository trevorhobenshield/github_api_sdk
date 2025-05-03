

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SocialAccountDeleteParams"]


class SocialAccountDeleteParams(TypedDict, total=False):
    account_urls: Required[list[str]]
    """Full URLs for the social media profiles to delete."""
