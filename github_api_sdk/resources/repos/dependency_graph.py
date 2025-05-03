from __future__ import annotations

from datetime import datetime
from typing import Dict, Union

import httpx

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.repos import dependency_graph_compare_params, dependency_graph_create_snapshot_params
from ...types.repos.dependency_graph_compare_response import DependencyGraphCompareResponse
from ...types.repos.dependency_graph_create_snapshot_response import DependencyGraphCreateSnapshotResponse
from ...types.repos.dependency_graph_export_sbom_response import DependencyGraphExportSbomResponse

__all__ = ["DependencyGraphResource", "AsyncDependencyGraphResource"]


class DependencyGraphResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DependencyGraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DependencyGraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DependencyGraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DependencyGraphResourceWithStreamingResponse(self)

    def compare(
        self,
        basehead: str,
        *,
        owner: str,
        repo: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependencyGraphCompareResponse:
        """
        Gets the diff of the dependency changes between two commits of a repository,
        based on the changes to the dependency manifests made in those commits.

        Args:
          name: The full path, relative to the repository root, of the dependency manifest file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not basehead:
            raise ValueError(f"Expected a non-empty value for `basehead` but received {basehead!r}")
        return self._get(
            f"/repos/{owner}/{repo}/dependency-graph/compare/{basehead}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, dependency_graph_compare_params.DependencyGraphCompareParams),
            ),
            cast_to=DependencyGraphCompareResponse,
        )

    def create_snapshot(
        self,
        repo: str,
        *,
        owner: str,
        detector: dependency_graph_create_snapshot_params.Detector,
        job: dependency_graph_create_snapshot_params.Job,
        ref: str,
        scanned: str | datetime,
        sha: str,
        version: int,
        manifests: dict[str, dependency_graph_create_snapshot_params.Manifests] | NotGiven = NOT_GIVEN,
        metadata: dict[str, str | float | bool | None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependencyGraphCreateSnapshotResponse:
        """
        Create a new snapshot of a repository's dependencies.

        The authenticated user must have access to the repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          detector: A description of the detector used.

          ref: The repository branch that triggered this snapshot.

          scanned: The time at which the snapshot was scanned.

          sha: The commit SHA associated with this dependency snapshot. Maximum length: 40
              characters.

          version: The version of the repository snapshot submission.

          manifests: A collection of package manifests, which are a collection of related
              dependencies declared in a file or representing a logical group of dependencies.

          metadata: User-defined metadata to store domain-specific information limited to 8 keys
              with scalar values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/dependency-graph/snapshots",
            body=maybe_transform(
                {
                    "detector": detector,
                    "job": job,
                    "ref": ref,
                    "scanned": scanned,
                    "sha": sha,
                    "version": version,
                    "manifests": manifests,
                    "metadata": metadata,
                },
                dependency_graph_create_snapshot_params.DependencyGraphCreateSnapshotParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependencyGraphCreateSnapshotResponse,
        )

    def export_sbom(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependencyGraphExportSbomResponse:
        """
        Exports the software bill of materials (SBOM) for a repository in SPDX JSON
        format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/dependency-graph/sbom",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependencyGraphExportSbomResponse,
        )


class AsyncDependencyGraphResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDependencyGraphResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDependencyGraphResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDependencyGraphResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDependencyGraphResourceWithStreamingResponse(self)

    async def compare(
        self,
        basehead: str,
        *,
        owner: str,
        repo: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependencyGraphCompareResponse:
        """
        Gets the diff of the dependency changes between two commits of a repository,
        based on the changes to the dependency manifests made in those commits.

        Args:
          name: The full path, relative to the repository root, of the dependency manifest file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not basehead:
            raise ValueError(f"Expected a non-empty value for `basehead` but received {basehead!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/dependency-graph/compare/{basehead}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"name": name}, dependency_graph_compare_params.DependencyGraphCompareParams),
            ),
            cast_to=DependencyGraphCompareResponse,
        )

    async def create_snapshot(
        self,
        repo: str,
        *,
        owner: str,
        detector: dependency_graph_create_snapshot_params.Detector,
        job: dependency_graph_create_snapshot_params.Job,
        ref: str,
        scanned: str | datetime,
        sha: str,
        version: int,
        manifests: dict[str, dependency_graph_create_snapshot_params.Manifests] | NotGiven = NOT_GIVEN,
        metadata: dict[str, str | float | bool | None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependencyGraphCreateSnapshotResponse:
        """
        Create a new snapshot of a repository's dependencies.

        The authenticated user must have access to the repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          detector: A description of the detector used.

          ref: The repository branch that triggered this snapshot.

          scanned: The time at which the snapshot was scanned.

          sha: The commit SHA associated with this dependency snapshot. Maximum length: 40
              characters.

          version: The version of the repository snapshot submission.

          manifests: A collection of package manifests, which are a collection of related
              dependencies declared in a file or representing a logical group of dependencies.

          metadata: User-defined metadata to store domain-specific information limited to 8 keys
              with scalar values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/dependency-graph/snapshots",
            body=await async_maybe_transform(
                {
                    "detector": detector,
                    "job": job,
                    "ref": ref,
                    "scanned": scanned,
                    "sha": sha,
                    "version": version,
                    "manifests": manifests,
                    "metadata": metadata,
                },
                dependency_graph_create_snapshot_params.DependencyGraphCreateSnapshotParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependencyGraphCreateSnapshotResponse,
        )

    async def export_sbom(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependencyGraphExportSbomResponse:
        """
        Exports the software bill of materials (SBOM) for a repository in SPDX JSON
        format.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/dependency-graph/sbom",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependencyGraphExportSbomResponse,
        )


class DependencyGraphResourceWithRawResponse:
    def __init__(self, dependency_graph: DependencyGraphResource) -> None:
        self._dependency_graph = dependency_graph

        self.compare = to_raw_response_wrapper(
            dependency_graph.compare,
        )
        self.create_snapshot = to_raw_response_wrapper(
            dependency_graph.create_snapshot,
        )
        self.export_sbom = to_raw_response_wrapper(
            dependency_graph.export_sbom,
        )


class AsyncDependencyGraphResourceWithRawResponse:
    def __init__(self, dependency_graph: AsyncDependencyGraphResource) -> None:
        self._dependency_graph = dependency_graph

        self.compare = async_to_raw_response_wrapper(
            dependency_graph.compare,
        )
        self.create_snapshot = async_to_raw_response_wrapper(
            dependency_graph.create_snapshot,
        )
        self.export_sbom = async_to_raw_response_wrapper(
            dependency_graph.export_sbom,
        )


class DependencyGraphResourceWithStreamingResponse:
    def __init__(self, dependency_graph: DependencyGraphResource) -> None:
        self._dependency_graph = dependency_graph

        self.compare = to_streamed_response_wrapper(
            dependency_graph.compare,
        )
        self.create_snapshot = to_streamed_response_wrapper(
            dependency_graph.create_snapshot,
        )
        self.export_sbom = to_streamed_response_wrapper(
            dependency_graph.export_sbom,
        )


class AsyncDependencyGraphResourceWithStreamingResponse:
    def __init__(self, dependency_graph: AsyncDependencyGraphResource) -> None:
        self._dependency_graph = dependency_graph

        self.compare = async_to_streamed_response_wrapper(
            dependency_graph.compare,
        )
        self.create_snapshot = async_to_streamed_response_wrapper(
            dependency_graph.create_snapshot,
        )
        self.export_sbom = async_to_streamed_response_wrapper(
            dependency_graph.export_sbom,
        )
