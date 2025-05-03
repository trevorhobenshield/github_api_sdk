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
from .._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ..types import license_list_params
from ..types.license_list_response import LicenseListResponse
from ..types.license_retrieve_response import LicenseRetrieveResponse

__all__ = ["LicensesResource", "AsyncLicensesResource"]


class LicensesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LicensesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return LicensesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LicensesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return LicensesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        license: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseRetrieveResponse:
        """Gets information about a specific license.

        For more information, see
        "[Licensing a repository ](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not license:
            raise ValueError(f"Expected a non-empty value for `license` but received {license!r}")
        return self._get(
            f"/licenses/{license}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LicenseRetrieveResponse,
        )

    def list(
        self,
        *,
        featured: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseListResponse:
        """Lists the most commonly used licenses on GitHub.

        For more information, see
        "[Licensing a repository ](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)."

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/licenses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "featured": featured,
                        "page": page,
                        "per_page": per_page,
                    },
                    license_list_params.LicenseListParams,
                ),
            ),
            cast_to=LicenseListResponse,
        )


class AsyncLicensesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLicensesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLicensesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLicensesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncLicensesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        license: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseRetrieveResponse:
        """Gets information about a specific license.

        For more information, see
        "[Licensing a repository ](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not license:
            raise ValueError(f"Expected a non-empty value for `license` but received {license!r}")
        return await self._get(
            f"/licenses/{license}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LicenseRetrieveResponse,
        )

    async def list(
        self,
        *,
        featured: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LicenseListResponse:
        """Lists the most commonly used licenses on GitHub.

        For more information, see
        "[Licensing a repository ](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)."

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/licenses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "featured": featured,
                        "page": page,
                        "per_page": per_page,
                    },
                    license_list_params.LicenseListParams,
                ),
            ),
            cast_to=LicenseListResponse,
        )


class LicensesResourceWithRawResponse:
    def __init__(self, licenses: LicensesResource) -> None:
        self._licenses = licenses

        self.retrieve = to_raw_response_wrapper(
            licenses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            licenses.list,
        )


class AsyncLicensesResourceWithRawResponse:
    def __init__(self, licenses: AsyncLicensesResource) -> None:
        self._licenses = licenses

        self.retrieve = async_to_raw_response_wrapper(
            licenses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            licenses.list,
        )


class LicensesResourceWithStreamingResponse:
    def __init__(self, licenses: LicensesResource) -> None:
        self._licenses = licenses

        self.retrieve = to_streamed_response_wrapper(
            licenses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            licenses.list,
        )


class AsyncLicensesResourceWithStreamingResponse:
    def __init__(self, licenses: AsyncLicensesResource) -> None:
        self._licenses = licenses

        self.retrieve = async_to_streamed_response_wrapper(
            licenses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            licenses.list,
        )
