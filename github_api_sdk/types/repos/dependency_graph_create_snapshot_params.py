

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DependencyGraphCreateSnapshotParams", "Detector", "Job", "Manifests", "ManifestsFile", "ManifestsResolved"]


class DependencyGraphCreateSnapshotParams(TypedDict, total=False):
    owner: Required[str]

    detector: Required[Detector]
    """A description of the detector used."""

    job: Required[Job]

    ref: Required[str]
    """The repository branch that triggered this snapshot."""

    scanned: Required[Annotated[str | datetime, PropertyInfo(format="iso8601")]]
    """The time at which the snapshot was scanned."""

    sha: Required[str]
    """The commit SHA associated with this dependency snapshot.

    Maximum length: 40 characters.
    """

    version: Required[int]
    """The version of the repository snapshot submission."""

    manifests: dict[str, Manifests]
    """
    A collection of package manifests, which are a collection of related
    dependencies declared in a file or representing a logical group of dependencies.
    """

    metadata: dict[str, str | float | bool | None]
    """
    User-defined metadata to store domain-specific information limited to 8 keys
    with scalar values.
    """


class Detector(TypedDict, total=False):
    name: Required[str]
    """The name of the detector used."""

    url: Required[str]
    """The url of the detector used."""

    version: Required[str]
    """The version of the detector used."""


class Job(TypedDict, total=False):
    id: Required[str]
    """The external ID of the job."""

    correlator: Required[str]
    """Correlator provides a key that is used to group snapshots submitted over time.

    Only the "latest" submitted snapshot for a given combination of `job.correlator`
    and `detector.name` will be considered when calculating a repository's current
    dependencies. Correlator should be as unique as it takes to distinguish all
    detection runs for a given "wave" of CI workflow you run. If you're using GitHub
    Actions, a good default value for this could be the environment variables
    GITHUB_WORKFLOW and GITHUB_JOB concatenated together. If you're using a build
    matrix, then you'll also need to add additional key(s) to distinguish between
    each submission inside a matrix variation.
    """

    html_url: str
    """The url for the job."""


class ManifestsFile(TypedDict, total=False):
    source_location: str
    """The path of the manifest file relative to the root of the Git repository."""


class ManifestsResolved(TypedDict, total=False):
    dependencies: list[str]
    """Array of package-url (PURLs) of direct child dependencies."""

    metadata: dict[str, str | float | bool | None]
    """
    User-defined metadata to store domain-specific information limited to 8 keys
    with scalar values.
    """

    package_url: str
    """Package-url (PURL) of dependency.

    See https://github.com/package-url/purl-spec for more details.
    """

    relationship: Literal["direct", "indirect"]
    """
    A notation of whether a dependency is requested directly by this manifest or is
    a dependency of another dependency.
    """

    scope: Literal["runtime", "development"]
    """
    A notation of whether the dependency is required for the primary build artifact
    (runtime) or is only used for development. Future versions of this specification
    may allow for more granular scopes.
    """


class Manifests(TypedDict, total=False):
    name: Required[str]
    """The name of the manifest."""

    file: ManifestsFile

    metadata: dict[str, str | float | bool | None]
    """
    User-defined metadata to store domain-specific information limited to 8 keys
    with scalar values.
    """

    resolved: dict[str, ManifestsResolved]
    """A collection of resolved package dependencies."""
