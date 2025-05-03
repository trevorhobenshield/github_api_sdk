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
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.repos import autolink_create_params
from ...types.repos.autolink import Autolink
from ...types.repos.autolink_list_response import AutolinkListResponse

__all__ = ["AutolinksResource", "AsyncAutolinksResource"]


class AutolinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutolinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AutolinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutolinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AutolinksResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        key_prefix: str,
        url_template: str,
        is_alphanumeric: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Autolink:
        """
        Users with admin access to the repository can create an autolink.

        Args:
          key_prefix: This prefix appended by certain characters will generate a link any time it is
              found in an issue, pull request, or commit.

          url_template: The URL must contain `<num>` for the reference number. `<num>` matches different
              characters depending on the value of `is_alphanumeric`.

          is_alphanumeric: Whether this autolink reference matches alphanumeric characters. If true, the
              `<num>` parameter of the `url_template` matches alphanumeric characters `A-Z`
              (case insensitive), `0-9`, and `-`. If false, this autolink reference only
              matches numeric characters.

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
            f"/repos/{owner}/{repo}/autolinks",
            body=maybe_transform(
                {
                    "key_prefix": key_prefix,
                    "url_template": url_template,
                    "is_alphanumeric": is_alphanumeric,
                },
                autolink_create_params.AutolinkCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Autolink,
        )

    def retrieve(
        self,
        autolink_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Autolink:
        """
        This returns a single autolink reference by ID that was configured for the given
        repository.

        Information about autolinks are only available to repository administrators.

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
            f"/repos/{owner}/{repo}/autolinks/{autolink_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Autolink,
        )

    def list(
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
    ) -> AutolinkListResponse:
        """
        Gets all autolinks that are configured for a repository.

        Information about autolinks are only available to repository administrators.

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
            f"/repos/{owner}/{repo}/autolinks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AutolinkListResponse,
        )

    def delete(
        self,
        autolink_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This deletes a single autolink reference by ID that was configured for the given
        repository.

        Information about autolinks are only available to repository administrators.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/autolinks/{autolink_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncAutolinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutolinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutolinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutolinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAutolinksResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        key_prefix: str,
        url_template: str,
        is_alphanumeric: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Autolink:
        """
        Users with admin access to the repository can create an autolink.

        Args:
          key_prefix: This prefix appended by certain characters will generate a link any time it is
              found in an issue, pull request, or commit.

          url_template: The URL must contain `<num>` for the reference number. `<num>` matches different
              characters depending on the value of `is_alphanumeric`.

          is_alphanumeric: Whether this autolink reference matches alphanumeric characters. If true, the
              `<num>` parameter of the `url_template` matches alphanumeric characters `A-Z`
              (case insensitive), `0-9`, and `-`. If false, this autolink reference only
              matches numeric characters.

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
            f"/repos/{owner}/{repo}/autolinks",
            body=await async_maybe_transform(
                {
                    "key_prefix": key_prefix,
                    "url_template": url_template,
                    "is_alphanumeric": is_alphanumeric,
                },
                autolink_create_params.AutolinkCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Autolink,
        )

    async def retrieve(
        self,
        autolink_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Autolink:
        """
        This returns a single autolink reference by ID that was configured for the given
        repository.

        Information about autolinks are only available to repository administrators.

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
            f"/repos/{owner}/{repo}/autolinks/{autolink_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Autolink,
        )

    async def list(
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
    ) -> AutolinkListResponse:
        """
        Gets all autolinks that are configured for a repository.

        Information about autolinks are only available to repository administrators.

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
            f"/repos/{owner}/{repo}/autolinks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AutolinkListResponse,
        )

    async def delete(
        self,
        autolink_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This deletes a single autolink reference by ID that was configured for the given
        repository.

        Information about autolinks are only available to repository administrators.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/autolinks/{autolink_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AutolinksResourceWithRawResponse:
    def __init__(self, autolinks: AutolinksResource) -> None:
        self._autolinks = autolinks

        self.create = to_raw_response_wrapper(
            autolinks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            autolinks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            autolinks.list,
        )
        self.delete = to_raw_response_wrapper(
            autolinks.delete,
        )


class AsyncAutolinksResourceWithRawResponse:
    def __init__(self, autolinks: AsyncAutolinksResource) -> None:
        self._autolinks = autolinks

        self.create = async_to_raw_response_wrapper(
            autolinks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            autolinks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            autolinks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            autolinks.delete,
        )


class AutolinksResourceWithStreamingResponse:
    def __init__(self, autolinks: AutolinksResource) -> None:
        self._autolinks = autolinks

        self.create = to_streamed_response_wrapper(
            autolinks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            autolinks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            autolinks.list,
        )
        self.delete = to_streamed_response_wrapper(
            autolinks.delete,
        )


class AsyncAutolinksResourceWithStreamingResponse:
    def __init__(self, autolinks: AsyncAutolinksResource) -> None:
        self._autolinks = autolinks

        self.create = async_to_streamed_response_wrapper(
            autolinks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            autolinks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            autolinks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            autolinks.delete,
        )
