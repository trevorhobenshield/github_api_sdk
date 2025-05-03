

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    owner: Required[str]

    oidc_token: Required[str]
    """
    The OIDC token issued by GitHub Actions certifying the origin of the deployment.
    """

    pages_build_version: Required[str]
    """A unique string that represents the version of the build for this deployment."""

    artifact_id: float
    """The ID of an artifact that contains the .zip or .tar of static assets to deploy.

    The artifact belongs to the repository. Either `artifact_id` or `artifact_url`
    are required.
    """

    artifact_url: str
    """The URL of an artifact that contains the .zip or .tar of static assets to
    deploy.

    The artifact belongs to the repository. Either `artifact_id` or `artifact_url`
    are required.
    """

    environment: str
    """The target environment for this GitHub Pages deployment."""
