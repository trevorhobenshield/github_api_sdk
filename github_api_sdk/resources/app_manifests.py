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
from ..types.app_manifest_create_conversion_response import AppManifestCreateConversionResponse

__all__ = ["AppManifestsResource", "AsyncAppManifestsResource"]


class AppManifestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppManifestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppManifestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppManifestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AppManifestsResourceWithStreamingResponse(self)

    def create_conversion(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppManifestCreateConversionResponse:
        """
        Use this endpoint to complete the handshake necessary when implementing the
        [GitHub App Manifest flow](https://docs.github.com/apps/building-github-apps/creating-github-apps-from-a-manifest/).
        When you create a GitHub App with the manifest flow, you receive a temporary
        `code` used to retrieve the GitHub App's `id`, `pem` (private key), and
        `webhook_secret`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._post(
            f"/app-manifests/{code}/conversions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppManifestCreateConversionResponse,
        )


class AsyncAppManifestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppManifestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppManifestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppManifestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAppManifestsResourceWithStreamingResponse(self)

    async def create_conversion(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppManifestCreateConversionResponse:
        """
        Use this endpoint to complete the handshake necessary when implementing the
        [GitHub App Manifest flow](https://docs.github.com/apps/building-github-apps/creating-github-apps-from-a-manifest/).
        When you create a GitHub App with the manifest flow, you receive a temporary
        `code` used to retrieve the GitHub App's `id`, `pem` (private key), and
        `webhook_secret`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._post(
            f"/app-manifests/{code}/conversions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppManifestCreateConversionResponse,
        )


class AppManifestsResourceWithRawResponse:
    def __init__(self, app_manifests: AppManifestsResource) -> None:
        self._app_manifests = app_manifests

        self.create_conversion = to_raw_response_wrapper(
            app_manifests.create_conversion,
        )


class AsyncAppManifestsResourceWithRawResponse:
    def __init__(self, app_manifests: AsyncAppManifestsResource) -> None:
        self._app_manifests = app_manifests

        self.create_conversion = async_to_raw_response_wrapper(
            app_manifests.create_conversion,
        )


class AppManifestsResourceWithStreamingResponse:
    def __init__(self, app_manifests: AppManifestsResource) -> None:
        self._app_manifests = app_manifests

        self.create_conversion = to_streamed_response_wrapper(
            app_manifests.create_conversion,
        )


class AsyncAppManifestsResourceWithStreamingResponse:
    def __init__(self, app_manifests: AsyncAppManifestsResource) -> None:
        self._app_manifests = app_manifests

        self.create_conversion = async_to_streamed_response_wrapper(
            app_manifests.create_conversion,
        )
