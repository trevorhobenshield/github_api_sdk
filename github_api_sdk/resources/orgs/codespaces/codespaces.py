from __future__ import annotations

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.orgs import codespace_list_params
from ....types.orgs.codespace_list_response import CodespaceListResponse
from .access.access import (
    AccessResource,
    AccessResourceWithRawResponse,
    AccessResourceWithStreamingResponse,
    AsyncAccessResource,
    AsyncAccessResourceWithRawResponse,
    AsyncAccessResourceWithStreamingResponse,
)
from .secrets.secrets import (
    AsyncSecretsResource,
    AsyncSecretsResourceWithRawResponse,
    AsyncSecretsResourceWithStreamingResponse,
    SecretsResource,
    SecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
)

__all__ = ["CodespacesResource", "AsyncCodespacesResource"]


class CodespacesResource(SyncAPIResource):
    @cached_property
    def access(self) -> AccessResource:
        return AccessResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CodespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodespacesResourceWithStreamingResponse(self)

    def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListResponse:
        """
        Lists the codespaces associated to a specified organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/codespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    codespace_list_params.CodespaceListParams,
                ),
            ),
            cast_to=CodespaceListResponse,
        )


class AsyncCodespacesResource(AsyncAPIResource):
    @cached_property
    def access(self) -> AsyncAccessResource:
        return AsyncAccessResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCodespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodespacesResourceWithStreamingResponse(self)

    async def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListResponse:
        """
        Lists the codespaces associated to a specified organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/codespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    codespace_list_params.CodespaceListParams,
                ),
            ),
            cast_to=CodespaceListResponse,
        )


class CodespacesResourceWithRawResponse:
    def __init__(self, codespaces: CodespacesResource) -> None:
        self._codespaces = codespaces

        self.list = to_raw_response_wrapper(
            codespaces.list,
        )

    @cached_property
    def access(self) -> AccessResourceWithRawResponse:
        return AccessResourceWithRawResponse(self._codespaces.access)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._codespaces.secrets)


class AsyncCodespacesResourceWithRawResponse:
    def __init__(self, codespaces: AsyncCodespacesResource) -> None:
        self._codespaces = codespaces

        self.list = async_to_raw_response_wrapper(
            codespaces.list,
        )

    @cached_property
    def access(self) -> AsyncAccessResourceWithRawResponse:
        return AsyncAccessResourceWithRawResponse(self._codespaces.access)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._codespaces.secrets)


class CodespacesResourceWithStreamingResponse:
    def __init__(self, codespaces: CodespacesResource) -> None:
        self._codespaces = codespaces

        self.list = to_streamed_response_wrapper(
            codespaces.list,
        )

    @cached_property
    def access(self) -> AccessResourceWithStreamingResponse:
        return AccessResourceWithStreamingResponse(self._codespaces.access)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._codespaces.secrets)


class AsyncCodespacesResourceWithStreamingResponse:
    def __init__(self, codespaces: AsyncCodespacesResource) -> None:
        self._codespaces = codespaces

        self.list = async_to_streamed_response_wrapper(
            codespaces.list,
        )

    @cached_property
    def access(self) -> AsyncAccessResourceWithStreamingResponse:
        return AsyncAccessResourceWithStreamingResponse(self._codespaces.access)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._codespaces.secrets)
