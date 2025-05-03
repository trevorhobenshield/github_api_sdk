

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RulesetRetrieveParams"]


class RulesetRetrieveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    includes_parents: bool
    """Include rulesets configured at higher levels that apply to this repository"""
