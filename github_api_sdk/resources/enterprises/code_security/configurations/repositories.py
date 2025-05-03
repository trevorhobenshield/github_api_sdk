from __future__ import annotations

import httpx

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.enterprises.code_security.configurations import repository_list_params
from .....types.enterprises.code_security.configurations.repository_list_response import RepositoryListResponse

__all__ = ["RepositoriesResource", "AsyncRepositoriesResource"]


class RepositoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RepositoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RepositoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RepositoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RepositoriesResourceWithStreamingResponse(self)

    def list(
        self,
        configuration_id: int,
        *,
        enterprise: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryListResponse:
        """
        Lists the repositories associated with an enterprise code security configuration
        in an organization.

        The authenticated user must be an administrator of the enterprise in order to
        use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `read:enterprise`
        scope to use this endpoint.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: A comma-separated list of statuses. If specified, only repositories with these
              attachment statuses will be returned.

              Can be: `all`, `attached`, `attaching`, `removed`, `enforced`, `failed`,
              `updating`, `removed_by_enterprise`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise:
            raise ValueError(f"Expected a non-empty value for `enterprise` but received {enterprise!r}")
        return self._get(
            f"/enterprises/{enterprise}/code-security/configurations/{configuration_id}/repositories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "status": status,
                    },
                    repository_list_params.RepositoryListParams,
                ),
            ),
            cast_to=RepositoryListResponse,
        )


class AsyncRepositoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRepositoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRepositoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRepositoriesResourceWithStreamingResponse(self)

    async def list(
        self,
        configuration_id: int,
        *,
        enterprise: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryListResponse:
        """
        Lists the repositories associated with an enterprise code security configuration
        in an organization.

        The authenticated user must be an administrator of the enterprise in order to
        use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `read:enterprise`
        scope to use this endpoint.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: A comma-separated list of statuses. If specified, only repositories with these
              attachment statuses will be returned.

              Can be: `all`, `attached`, `attaching`, `removed`, `enforced`, `failed`,
              `updating`, `removed_by_enterprise`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise:
            raise ValueError(f"Expected a non-empty value for `enterprise` but received {enterprise!r}")
        return await self._get(
            f"/enterprises/{enterprise}/code-security/configurations/{configuration_id}/repositories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "status": status,
                    },
                    repository_list_params.RepositoryListParams,
                ),
            ),
            cast_to=RepositoryListResponse,
        )


class RepositoriesResourceWithRawResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.list = to_raw_response_wrapper(
            repositories.list,
        )


class AsyncRepositoriesResourceWithRawResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.list = async_to_raw_response_wrapper(
            repositories.list,
        )


class RepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.list = to_streamed_response_wrapper(
            repositories.list,
        )


class AsyncRepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.list = async_to_streamed_response_wrapper(
            repositories.list,
        )
