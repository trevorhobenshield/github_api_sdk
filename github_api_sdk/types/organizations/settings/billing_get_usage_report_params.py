

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BillingGetUsageReportParams"]


class BillingGetUsageReportParams(TypedDict, total=False):
    day: int
    """If specified, only return results for a single day.

    The value of `day` is an integer between `1` and `31`. If no `year` or `month`
    is specified, the default `year` and `month` are used.
    """

    hour: int
    """If specified, only return results for a single hour.

    The value of `hour` is an integer between `0` and `23`. If no `year`, `month`,
    or `day` is specified, the default `year`, `month`, and `day` are used.
    """

    month: int
    """If specified, only return results for a single month.

    The value of `month` is an integer between `1` and `12`. If no year is specified
    the default `year` is used.
    """

    year: int
    """If specified, only return results for a single year.

    The value of `year` is an integer with four digits representing a year. For
    example, `2025`. Default value is the current year.
    """
