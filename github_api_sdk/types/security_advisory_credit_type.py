

from typing_extensions import Literal, TypeAlias

__all__ = ["SecurityAdvisoryCreditType"]

SecurityAdvisoryCreditType: TypeAlias = Literal[
    "analyst",
    "finder",
    "reporter",
    "coordinator",
    "remediation_developer",
    "remediation_reviewer",
    "remediation_verifier",
    "tool",
    "sponsor",
    "other",
]
