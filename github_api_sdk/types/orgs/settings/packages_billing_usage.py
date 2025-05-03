


from ...._models import BaseModel

__all__ = ["PackagesBillingUsage"]


class PackagesBillingUsage(BaseModel):
    included_gigabytes_bandwidth: int
    """Free storage space (GB) for GitHub Packages."""

    total_gigabytes_bandwidth_used: int
    """Sum of the free and paid storage space (GB) for GitHuub Packages."""

    total_paid_gigabytes_bandwidth_used: int
    """Total paid storage space (GB) for GitHuub Packages."""
