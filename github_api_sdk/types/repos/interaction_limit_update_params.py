

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..orgs.interaction_group import InteractionGroup

__all__ = ["InteractionLimitUpdateParams"]


class InteractionLimitUpdateParams(TypedDict, total=False):
    owner: Required[str]

    limit: Required[InteractionGroup]
    """
    The type of GitHub user that can comment, open issues, or create pull requests
    while the interaction limit is in effect.
    """

    expiry: Literal["one_day", "three_days", "one_week", "one_month", "six_months"]
    """The duration of the interaction restriction. Default: `one_day`."""
