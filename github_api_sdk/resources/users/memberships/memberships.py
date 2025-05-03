from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .orgs import (
    AsyncOrgsResource,
    AsyncOrgsResourceWithRawResponse,
    AsyncOrgsResourceWithStreamingResponse,
    OrgsResource,
    OrgsResourceWithRawResponse,
    OrgsResourceWithStreamingResponse,
)

__all__ = ["MembershipsResource", "AsyncMembershipsResource"]


class MembershipsResource(SyncAPIResource):
    @cached_property
    def orgs(self) -> OrgsResource:
        return OrgsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MembershipsResourceWithStreamingResponse(self)


class AsyncMembershipsResource(AsyncAPIResource):
    @cached_property
    def orgs(self) -> AsyncOrgsResource:
        return AsyncOrgsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMembershipsResourceWithStreamingResponse(self)


class MembershipsResourceWithRawResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

    @cached_property
    def orgs(self) -> OrgsResourceWithRawResponse:
        return OrgsResourceWithRawResponse(self._memberships.orgs)


class AsyncMembershipsResourceWithRawResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

    @cached_property
    def orgs(self) -> AsyncOrgsResourceWithRawResponse:
        return AsyncOrgsResourceWithRawResponse(self._memberships.orgs)


class MembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

    @cached_property
    def orgs(self) -> OrgsResourceWithStreamingResponse:
        return OrgsResourceWithStreamingResponse(self._memberships.orgs)


class AsyncMembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

    @cached_property
    def orgs(self) -> AsyncOrgsResourceWithStreamingResponse:
        return AsyncOrgsResourceWithStreamingResponse(self._memberships.orgs)
