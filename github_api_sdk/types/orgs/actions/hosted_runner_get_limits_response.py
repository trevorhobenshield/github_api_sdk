


from ...._models import BaseModel

__all__ = ["HostedRunnerGetLimitsResponse", "PublicIPs"]


class PublicIPs(BaseModel):
    current_usage: int
    """The current number of static public IP addresses in use by Hosted Runners."""

    maximum: int
    """
    The maximum number of static public IP addresses that can be used for Hosted
    Runners.
    """


class HostedRunnerGetLimitsResponse(BaseModel):
    public_ips: PublicIPs
    """Provides details of static public IP limits for GitHub-hosted Hosted Runners"""
