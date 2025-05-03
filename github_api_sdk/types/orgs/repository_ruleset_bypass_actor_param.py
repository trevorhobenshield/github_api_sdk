

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRulesetBypassActorParam"]


class RepositoryRulesetBypassActorParam(TypedDict, total=False):
    actor_type: Required[Literal["Integration", "OrganizationAdmin", "RepositoryRole", "Team", "DeployKey"]]
    """The type of actor that can bypass a ruleset."""

    actor_id: int | None
    """The ID of the actor that can bypass a ruleset.

    If `actor_type` is `OrganizationAdmin`, this should be `1`. If `actor_type` is
    `DeployKey`, this should be null. `OrganizationAdmin` is not applicable for
    personal repositories.
    """

    bypass_mode: Literal["always", "pull_request"]
    """When the specified actor can bypass the ruleset.

    `pull_request` means that an actor can only bypass rules on pull requests.
    `pull_request` is not applicable for the `DeployKey` actor type. Also,
    `pull_request` is only applicable to branch rulesets.
    """
