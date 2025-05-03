from __future__ import annotations

from typing import List, Optional

import httpx
from typing_extensions import Literal

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
from ....types.repos.code_scanning import default_setup_update_params
from ....types.repos.code_scanning.default_setup_retrieve_response import DefaultSetupRetrieveResponse

__all__ = ["DefaultSetupResource", "AsyncDefaultSetupResource"]


class DefaultSetupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefaultSetupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DefaultSetupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultSetupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DefaultSetupResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> DefaultSetupRetrieveResponse:
        """
        Gets a code scanning default setup configuration.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

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
            f"/repos/{owner}/{repo}/code-scanning/default-setup",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DefaultSetupRetrieveResponse,
        )

    def update(
        self,
        repo: str,
        *,
        owner: str,
        languages: list[Literal["actions", "c-cpp", "csharp", "go", "java-kotlin", "javascript-typescript", "python", "ruby", "swift"]]
        | NotGiven = NOT_GIVEN,
        query_suite: Literal["default", "extended"] | NotGiven = NOT_GIVEN,
        runner_label: str | None | NotGiven = NOT_GIVEN,
        runner_type: Literal["standard", "labeled"] | NotGiven = NOT_GIVEN,
        state: Literal["configured", "not-configured"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates a code scanning default setup configuration.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
          languages: CodeQL languages to be analyzed.

          query_suite: CodeQL query suite to be used.

          runner_label: Runner label to be used if the runner type is labeled.

          runner_type: Runner type to be used.

          state: The desired state of code scanning default setup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/code-scanning/default-setup",
            body=maybe_transform(
                {
                    "languages": languages,
                    "query_suite": query_suite,
                    "runner_label": runner_label,
                    "runner_type": runner_type,
                    "state": state,
                },
                default_setup_update_params.DefaultSetupUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class AsyncDefaultSetupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefaultSetupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultSetupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultSetupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDefaultSetupResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> DefaultSetupRetrieveResponse:
        """
        Gets a code scanning default setup configuration.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

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
            f"/repos/{owner}/{repo}/code-scanning/default-setup",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DefaultSetupRetrieveResponse,
        )

    async def update(
        self,
        repo: str,
        *,
        owner: str,
        languages: list[Literal["actions", "c-cpp", "csharp", "go", "java-kotlin", "javascript-typescript", "python", "ruby", "swift"]]
        | NotGiven = NOT_GIVEN,
        query_suite: Literal["default", "extended"] | NotGiven = NOT_GIVEN,
        runner_label: str | None | NotGiven = NOT_GIVEN,
        runner_type: Literal["standard", "labeled"] | NotGiven = NOT_GIVEN,
        state: Literal["configured", "not-configured"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates a code scanning default setup configuration.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
          languages: CodeQL languages to be analyzed.

          query_suite: CodeQL query suite to be used.

          runner_label: Runner label to be used if the runner type is labeled.

          runner_type: Runner type to be used.

          state: The desired state of code scanning default setup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/code-scanning/default-setup",
            body=await async_maybe_transform(
                {
                    "languages": languages,
                    "query_suite": query_suite,
                    "runner_label": runner_label,
                    "runner_type": runner_type,
                    "state": state,
                },
                default_setup_update_params.DefaultSetupUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class DefaultSetupResourceWithRawResponse:
    def __init__(self, default_setup: DefaultSetupResource) -> None:
        self._default_setup = default_setup

        self.retrieve = to_raw_response_wrapper(
            default_setup.retrieve,
        )
        self.update = to_raw_response_wrapper(
            default_setup.update,
        )


class AsyncDefaultSetupResourceWithRawResponse:
    def __init__(self, default_setup: AsyncDefaultSetupResource) -> None:
        self._default_setup = default_setup

        self.retrieve = async_to_raw_response_wrapper(
            default_setup.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            default_setup.update,
        )


class DefaultSetupResourceWithStreamingResponse:
    def __init__(self, default_setup: DefaultSetupResource) -> None:
        self._default_setup = default_setup

        self.retrieve = to_streamed_response_wrapper(
            default_setup.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            default_setup.update,
        )


class AsyncDefaultSetupResourceWithStreamingResponse:
    def __init__(self, default_setup: AsyncDefaultSetupResource) -> None:
        self._default_setup = default_setup

        self.retrieve = async_to_streamed_response_wrapper(
            default_setup.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            default_setup.update,
        )
