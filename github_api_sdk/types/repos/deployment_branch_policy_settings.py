


from ..._models import BaseModel

__all__ = ["DeploymentBranchPolicySettings"]


class DeploymentBranchPolicySettings(BaseModel):
    custom_branch_policies: bool
    """
    Whether only branches that match the specified name patterns can deploy to this
    environment. If `custom_branch_policies` is `true`, `protected_branches` must be
    `false`; if `custom_branch_policies` is `false`, `protected_branches` must be
    `true`.
    """

    protected_branches: bool
    """
    Whether only branches with branch protection rules can deploy to this
    environment. If `protected_branches` is `true`, `custom_branch_policies` must be
    `false`; if `protected_branches` is `false`, `custom_branch_policies` must be
    `true`.
    """
