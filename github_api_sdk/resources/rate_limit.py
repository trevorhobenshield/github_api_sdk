from __future__ import annotations

import httpx

from .._base_client import make_request_options
from .._compat import cached_property
from .._resource import AsyncAPIResource, SyncAPIResource
from .._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..types.rate_limit_retrieve_response import RateLimitRetrieveResponse

__all__ = ["RateLimitResource", "AsyncRateLimitResource"]


class RateLimitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RateLimitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RateLimitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RateLimitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RateLimitResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateLimitRetrieveResponse:
        """
        > [!NOTE] Accessing this endpoint does not count against your REST API rate
        > limit.

        Some categories of endpoints have custom rate limits that are separate from the
        rate limit governing the other REST API endpoints. For this reason, the API
        response categorizes your rate limit. Under `resources`, you'll see objects
        relating to different categories:

        - The `core` object provides your rate limit status for all non-search-related
          resources in the REST API.
        - The `search` object provides your rate limit status for the REST API for
          searching (excluding code searches). For more information, see
          "[Search](https://docs.github.com/rest/search/search)."
        - The `code_search` object provides your rate limit status for the REST API for
          searching code. For more information, see
          "[Search code](https://docs.github.com/rest/search/search#search-code)."
        - The `graphql` object provides your rate limit status for the GraphQL API. For
          more information, see
          "[Resource limitations](https://docs.github.com/graphql/overview/resource-limitations#rate-limit)."
        - The `integration_manifest` object provides your rate limit status for the
          `POST /app-manifests/{code}/conversions` operation. For more information, see
          "[Creating a GitHub App from a manifest](https://docs.github.com/apps/creating-github-apps/setting-up-a-github-app/creating-a-github-app-from-a-manifest#3-you-exchange-the-temporary-code-to-retrieve-the-app-configuration)."
        - The `dependency_snapshots` object provides your rate limit status for
          submitting snapshots to the dependency graph. For more information, see
          "[Dependency graph](https://docs.github.com/rest/dependency-graph)."
        - The `code_scanning_upload` object provides your rate limit status for
          uploading SARIF results to code scanning. For more information, see
          "[Uploading a SARIF file to GitHub](https://docs.github.com/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)."
        - The `actions_runner_registration` object provides your rate limit status for
          registering self-hosted runners in GitHub Actions. For more information, see
          "[Self-hosted runners](https://docs.github.com/rest/actions/self-hosted-runners)."
        - The `source_import` object is no longer in use for any API endpoints, and it
          will be removed in the next API version. For more information about API
          versions, see
          "[API Versions](https://docs.github.com/rest/about-the-rest-api/api-versions)."

        > [!NOTE] The `rate` object is closing down. If you're writing new API client
        > code or updating existing code, you should use the `core` object instead of
        > the `rate` object. The `core` object contains the same information that is
        > present in the `rate` object.
        """
        return self._get(
            "/rate_limit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RateLimitRetrieveResponse,
        )


class AsyncRateLimitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRateLimitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRateLimitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRateLimitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRateLimitResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateLimitRetrieveResponse:
        """
        > [!NOTE] Accessing this endpoint does not count against your REST API rate
        > limit.

        Some categories of endpoints have custom rate limits that are separate from the
        rate limit governing the other REST API endpoints. For this reason, the API
        response categorizes your rate limit. Under `resources`, you'll see objects
        relating to different categories:

        - The `core` object provides your rate limit status for all non-search-related
          resources in the REST API.
        - The `search` object provides your rate limit status for the REST API for
          searching (excluding code searches). For more information, see
          "[Search](https://docs.github.com/rest/search/search)."
        - The `code_search` object provides your rate limit status for the REST API for
          searching code. For more information, see
          "[Search code](https://docs.github.com/rest/search/search#search-code)."
        - The `graphql` object provides your rate limit status for the GraphQL API. For
          more information, see
          "[Resource limitations](https://docs.github.com/graphql/overview/resource-limitations#rate-limit)."
        - The `integration_manifest` object provides your rate limit status for the
          `POST /app-manifests/{code}/conversions` operation. For more information, see
          "[Creating a GitHub App from a manifest](https://docs.github.com/apps/creating-github-apps/setting-up-a-github-app/creating-a-github-app-from-a-manifest#3-you-exchange-the-temporary-code-to-retrieve-the-app-configuration)."
        - The `dependency_snapshots` object provides your rate limit status for
          submitting snapshots to the dependency graph. For more information, see
          "[Dependency graph](https://docs.github.com/rest/dependency-graph)."
        - The `code_scanning_upload` object provides your rate limit status for
          uploading SARIF results to code scanning. For more information, see
          "[Uploading a SARIF file to GitHub](https://docs.github.com/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)."
        - The `actions_runner_registration` object provides your rate limit status for
          registering self-hosted runners in GitHub Actions. For more information, see
          "[Self-hosted runners](https://docs.github.com/rest/actions/self-hosted-runners)."
        - The `source_import` object is no longer in use for any API endpoints, and it
          will be removed in the next API version. For more information about API
          versions, see
          "[API Versions](https://docs.github.com/rest/about-the-rest-api/api-versions)."

        > [!NOTE] The `rate` object is closing down. If you're writing new API client
        > code or updating existing code, you should use the `core` object instead of
        > the `rate` object. The `core` object contains the same information that is
        > present in the `rate` object.
        """
        return await self._get(
            "/rate_limit",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RateLimitRetrieveResponse,
        )


class RateLimitResourceWithRawResponse:
    def __init__(self, rate_limit: RateLimitResource) -> None:
        self._rate_limit = rate_limit

        self.retrieve = to_raw_response_wrapper(
            rate_limit.retrieve,
        )


class AsyncRateLimitResourceWithRawResponse:
    def __init__(self, rate_limit: AsyncRateLimitResource) -> None:
        self._rate_limit = rate_limit

        self.retrieve = async_to_raw_response_wrapper(
            rate_limit.retrieve,
        )


class RateLimitResourceWithStreamingResponse:
    def __init__(self, rate_limit: RateLimitResource) -> None:
        self._rate_limit = rate_limit

        self.retrieve = to_streamed_response_wrapper(
            rate_limit.retrieve,
        )


class AsyncRateLimitResourceWithStreamingResponse:
    def __init__(self, rate_limit: AsyncRateLimitResource) -> None:
        self._rate_limit = rate_limit

        self.retrieve = async_to_streamed_response_wrapper(
            rate_limit.retrieve,
        )
