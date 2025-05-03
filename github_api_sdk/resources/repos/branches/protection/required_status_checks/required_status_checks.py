from __future__ import annotations

from typing import Iterable, List

import httpx

from ......_base_client import make_request_options
from ......_compat import cached_property
from ......_resource import AsyncAPIResource, SyncAPIResource
from ......_response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ......_types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ......_utils import (
    async_maybe_transform,
    maybe_transform,
)
from ......types.repos.branches.protection import required_status_check_update_params
from ......types.repos.branches.protection.status_check_policy import StatusCheckPolicy
from .contexts import (
    AsyncContextsResource,
    AsyncContextsResourceWithRawResponse,
    AsyncContextsResourceWithStreamingResponse,
    ContextsResource,
    ContextsResourceWithRawResponse,
    ContextsResourceWithStreamingResponse,
)

__all__ = ["RequiredStatusChecksResource", "AsyncRequiredStatusChecksResource"]


class RequiredStatusChecksResource(SyncAPIResource):
    @cached_property
    def contexts(self) -> ContextsResource:
        return ContextsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RequiredStatusChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RequiredStatusChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequiredStatusChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RequiredStatusChecksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusCheckPolicy:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return self._get(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatusCheckPolicy,
        )

    def update(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        checks: Iterable[required_status_check_update_params.Check] | NotGiven = NOT_GIVEN,
        contexts: list[str] | NotGiven = NOT_GIVEN,
        strict: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusCheckPolicy:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Updating required status checks requires admin or owner permissions to the
        repository and branch protection to be enabled.

        Args:
          checks: The list of status checks to require in order to merge into this branch.

          contexts: **Closing down notice**: The list of status checks to require in order to merge
              into this branch. If any of these checks have recently been set by a particular
              GitHub App, they will be required to come from that app in future for the branch
              to merge. Use `checks` instead of `contexts` for more fine-grained control.

          strict: Require branches to be up to date before merging.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
            body=maybe_transform(
                {
                    "checks": checks,
                    "contexts": contexts,
                    "strict": strict,
                },
                required_status_check_update_params.RequiredStatusCheckUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatusCheckPolicy,
        )

    def remove(
        self,
        branch: str,
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
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncRequiredStatusChecksResource(AsyncAPIResource):
    @cached_property
    def contexts(self) -> AsyncContextsResource:
        return AsyncContextsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequiredStatusChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequiredStatusChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequiredStatusChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRequiredStatusChecksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusCheckPolicy:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatusCheckPolicy,
        )

    async def update(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        checks: Iterable[required_status_check_update_params.Check] | NotGiven = NOT_GIVEN,
        contexts: list[str] | NotGiven = NOT_GIVEN,
        strict: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusCheckPolicy:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Updating required status checks requires admin or owner permissions to the
        repository and branch protection to be enabled.

        Args:
          checks: The list of status checks to require in order to merge into this branch.

          contexts: **Closing down notice**: The list of status checks to require in order to merge
              into this branch. If any of these checks have recently been set by a particular
              GitHub App, they will be required to come from that app in future for the branch
              to merge. Use `checks` instead of `contexts` for more fine-grained control.

          strict: Require branches to be up to date before merging.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
            body=await async_maybe_transform(
                {
                    "checks": checks,
                    "contexts": contexts,
                    "strict": strict,
                },
                required_status_check_update_params.RequiredStatusCheckUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatusCheckPolicy,
        )

    async def remove(
        self,
        branch: str,
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
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class RequiredStatusChecksResourceWithRawResponse:
    def __init__(self, required_status_checks: RequiredStatusChecksResource) -> None:
        self._required_status_checks = required_status_checks

        self.retrieve = to_raw_response_wrapper(
            required_status_checks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            required_status_checks.update,
        )
        self.remove = to_raw_response_wrapper(
            required_status_checks.remove,
        )

    @cached_property
    def contexts(self) -> ContextsResourceWithRawResponse:
        return ContextsResourceWithRawResponse(self._required_status_checks.contexts)


class AsyncRequiredStatusChecksResourceWithRawResponse:
    def __init__(self, required_status_checks: AsyncRequiredStatusChecksResource) -> None:
        self._required_status_checks = required_status_checks

        self.retrieve = async_to_raw_response_wrapper(
            required_status_checks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            required_status_checks.update,
        )
        self.remove = async_to_raw_response_wrapper(
            required_status_checks.remove,
        )

    @cached_property
    def contexts(self) -> AsyncContextsResourceWithRawResponse:
        return AsyncContextsResourceWithRawResponse(self._required_status_checks.contexts)


class RequiredStatusChecksResourceWithStreamingResponse:
    def __init__(self, required_status_checks: RequiredStatusChecksResource) -> None:
        self._required_status_checks = required_status_checks

        self.retrieve = to_streamed_response_wrapper(
            required_status_checks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            required_status_checks.update,
        )
        self.remove = to_streamed_response_wrapper(
            required_status_checks.remove,
        )

    @cached_property
    def contexts(self) -> ContextsResourceWithStreamingResponse:
        return ContextsResourceWithStreamingResponse(self._required_status_checks.contexts)


class AsyncRequiredStatusChecksResourceWithStreamingResponse:
    def __init__(self, required_status_checks: AsyncRequiredStatusChecksResource) -> None:
        self._required_status_checks = required_status_checks

        self.retrieve = async_to_streamed_response_wrapper(
            required_status_checks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            required_status_checks.update,
        )
        self.remove = async_to_streamed_response_wrapper(
            required_status_checks.remove,
        )

    @cached_property
    def contexts(self) -> AsyncContextsResourceWithStreamingResponse:
        return AsyncContextsResourceWithStreamingResponse(self._required_status_checks.contexts)
