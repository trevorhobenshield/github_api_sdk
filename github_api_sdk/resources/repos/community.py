from __future__ import annotations

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
from ...types.repos.community_retrieve_profile_response import CommunityRetrieveProfileResponse

__all__ = ["CommunityResource", "AsyncCommunityResource"]


class CommunityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommunityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommunityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommunityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CommunityResourceWithStreamingResponse(self)

    def retrieve_profile(
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
    ) -> CommunityRetrieveProfileResponse:
        """Returns all community profile metrics for a repository.

        The repository cannot be
        a fork.

        The returned metrics include an overall health score, the repository
        description, the presence of documentation, the detected code of conduct, the
        detected license, and the presence of ISSUE_TEMPLATE, PULL_REQUEST_TEMPLATE,
        README, and CONTRIBUTING files.

        The `health_percentage` score is defined as a percentage of how many of the
        recommended community health files are present. For more information, see
        "[About community profiles for public repositories](https://docs.github.com/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)."

        `content_reports_enabled` is only returned for organization-owned repositories.

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
            f"/repos/{owner}/{repo}/community/profile",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CommunityRetrieveProfileResponse,
        )


class AsyncCommunityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommunityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommunityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommunityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCommunityResourceWithStreamingResponse(self)

    async def retrieve_profile(
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
    ) -> CommunityRetrieveProfileResponse:
        """Returns all community profile metrics for a repository.

        The repository cannot be
        a fork.

        The returned metrics include an overall health score, the repository
        description, the presence of documentation, the detected code of conduct, the
        detected license, and the presence of ISSUE_TEMPLATE, PULL_REQUEST_TEMPLATE,
        README, and CONTRIBUTING files.

        The `health_percentage` score is defined as a percentage of how many of the
        recommended community health files are present. For more information, see
        "[About community profiles for public repositories](https://docs.github.com/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories)."

        `content_reports_enabled` is only returned for organization-owned repositories.

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
            f"/repos/{owner}/{repo}/community/profile",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CommunityRetrieveProfileResponse,
        )


class CommunityResourceWithRawResponse:
    def __init__(self, community: CommunityResource) -> None:
        self._community = community

        self.retrieve_profile = to_raw_response_wrapper(
            community.retrieve_profile,
        )


class AsyncCommunityResourceWithRawResponse:
    def __init__(self, community: AsyncCommunityResource) -> None:
        self._community = community

        self.retrieve_profile = async_to_raw_response_wrapper(
            community.retrieve_profile,
        )


class CommunityResourceWithStreamingResponse:
    def __init__(self, community: CommunityResource) -> None:
        self._community = community

        self.retrieve_profile = to_streamed_response_wrapper(
            community.retrieve_profile,
        )


class AsyncCommunityResourceWithStreamingResponse:
    def __init__(self, community: AsyncCommunityResource) -> None:
        self._community = community

        self.retrieve_profile = async_to_streamed_response_wrapper(
            community.retrieve_profile,
        )
