

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrgSetSecurityFeatureParams"]


class OrgSetSecurityFeatureParams(TypedDict, total=False):
    org: Required[str]

    security_product: Required[
        Literal[
            "dependency_graph",
            "dependabot_alerts",
            "dependabot_security_updates",
            "advanced_security",
            "code_scanning_default_setup",
            "secret_scanning",
            "secret_scanning_push_protection",
        ]
    ]

    query_suite: Literal["default", "extended"]
    """CodeQL query suite to be used.

    If you specify the `query_suite` parameter, the default setup will be configured
    with this query suite only on all repositories that didn't have default setup
    already configured. It will not change the query suite on repositories that
    already have default setup configured. If you don't specify any `query_suite` in
    your request, the preferred query suite of the organization will be applied.
    """
