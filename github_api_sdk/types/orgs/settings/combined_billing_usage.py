


from ...._models import BaseModel

__all__ = ["CombinedBillingUsage"]


class CombinedBillingUsage(BaseModel):
    days_left_in_billing_cycle: int
    """Numbers of days left in billing cycle."""

    estimated_paid_storage_for_month: int
    """Estimated storage space (GB) used in billing cycle."""

    estimated_storage_for_month: int
    """Estimated sum of free and paid storage space (GB) used in billing cycle."""
