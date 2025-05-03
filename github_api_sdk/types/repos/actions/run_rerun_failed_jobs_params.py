

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunRerunFailedJobsParams"]


class RunRerunFailedJobsParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    enable_debug_logging: bool
    """Whether to enable debug logging for the re-run."""
