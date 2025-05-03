

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..orgs.repository_rule_param import RepositoryRuleParam
from ..orgs.repository_rule_enforcement import RepositoryRuleEnforcement
from .repository_ruleset_conditions_param import RepositoryRulesetConditionsParam
from ..orgs.repository_ruleset_bypass_actor_param import RepositoryRulesetBypassActorParam

__all__ = ["RulesetCreateParams"]


class RulesetCreateParams(TypedDict, total=False):
    owner: Required[str]

    enforcement: Required[RepositoryRuleEnforcement]
    """The enforcement level of the ruleset.

    `evaluate` allows admins to test rules before enforcing them. Admins can view
    insights on the Rule Insights page (`evaluate` is only available with GitHub
    Enterprise).
    """

    name: Required[str]
    """The name of the ruleset."""

    bypass_actors: Iterable[RepositoryRulesetBypassActorParam]
    """The actors that can bypass the rules in this ruleset"""

    conditions: RepositoryRulesetConditionsParam
    """Parameters for a repository ruleset ref name condition"""

    rules: Iterable[RepositoryRuleParam]
    """An array of rules within the ruleset."""

    target: Literal["branch", "tag", "push"]
    """The target of the ruleset"""
