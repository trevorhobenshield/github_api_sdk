

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .repository_rule_param import RepositoryRuleParam
from .repository_rule_enforcement import RepositoryRuleEnforcement
from .org_ruleset_conditions_param import OrgRulesetConditionsParam
from .repository_ruleset_bypass_actor_param import RepositoryRulesetBypassActorParam

__all__ = ["RulesetUpdateParams"]


class RulesetUpdateParams(TypedDict, total=False):
    org: Required[str]

    bypass_actors: Iterable[RepositoryRulesetBypassActorParam]
    """The actors that can bypass the rules in this ruleset"""

    conditions: OrgRulesetConditionsParam
    """
    Conditions for an organization ruleset. The branch and tag rulesets conditions
    object should contain both `repository_name` and `ref_name` properties, or both
    `repository_id` and `ref_name` properties, or both `repository_property` and
    `ref_name` properties. The push rulesets conditions object does not require the
    `ref_name` property. For repository policy rulesets, the conditions object
    should only contain the `repository_name`, the `repository_id`, or the
    `repository_property`.
    """

    enforcement: RepositoryRuleEnforcement
    """The enforcement level of the ruleset.

    `evaluate` allows admins to test rules before enforcing them. Admins can view
    insights on the Rule Insights page (`evaluate` is only available with GitHub
    Enterprise).
    """

    name: str
    """The name of the ruleset."""

    rules: Iterable[RepositoryRuleParam]
    """An array of rules within the ruleset."""

    target: Literal["branch", "tag", "push", "repository"]
    """The target of the ruleset"""
