

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeploymentProtectionRuleCreateParams"]


class DeploymentProtectionRuleCreateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    integration_id: int
    """The ID of the custom app that will be enabled on the environment."""
