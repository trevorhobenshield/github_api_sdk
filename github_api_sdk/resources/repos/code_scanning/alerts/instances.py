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
from .....types.repos.code_scanning.alerts import instance_list_params
from .....types.repos.code_scanning.alerts.instance_list_response import InstanceListResponse

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def list(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        pr: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstanceListResponse:
        """
        Lists all instances of the specified code scanning alert.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          pr: The number of the pull request for the results you want to list.

          ref: The Git reference for the results you want to list. The `ref` for a branch can
              be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To
              reference a pull request use `refs/pull/<number>/merge`.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "pr": pr,
                        "ref": ref,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            cast_to=InstanceListResponse,
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    async def list(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        pr: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstanceListResponse:
        """
        Lists all instances of the specified code scanning alert.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          pr: The number of the pull request for the results you want to list.

          ref: The Git reference for the results you want to list. The `ref` for a branch can
              be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To
              reference a pull request use `refs/pull/<number>/merge`.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "pr": pr,
                        "ref": ref,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            cast_to=InstanceListResponse,
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.list = to_raw_response_wrapper(
            instances.list,
        )


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.list = async_to_raw_response_wrapper(
            instances.list,
        )


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.list = to_streamed_response_wrapper(
            instances.list,
        )


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.list = async_to_streamed_response_wrapper(
            instances.list,
        )
