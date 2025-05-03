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
from .....types.repos.code_scanning.alerts import autofix_commit_params
from .....types.repos.code_scanning.alerts.autofix_commit_response import AutofixCommitResponse
from .....types.repos.code_scanning.alerts.code_scanning_autofix import CodeScanningAutofix

__all__ = ["AutofixResource", "AsyncAutofixResource"]


class AutofixResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutofixResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AutofixResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutofixResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AutofixResourceWithStreamingResponse(self)

    def create(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningAutofix:
        """
        Creates an autofix for a code scanning alert.

        If a new autofix is to be created as a result of this request or is currently
        being generated, then this endpoint will return a 202 Accepted response.

        If an autofix already exists for a given alert, then this endpoint will return a
        200 OK response.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningAutofix,
        )

    def retrieve(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningAutofix:
        """
        Gets the status and description of an autofix for a code scanning alert.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningAutofix,
        )

    def commit(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        message: str | NotGiven = NOT_GIVEN,
        target_ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutofixCommitResponse:
        """
        Commits an autofix for a code scanning alert.

        If an autofix is committed as a result of this request, then this endpoint will
        return a 201 Created response.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

          message: Commit message to be used.

          target_ref: The Git reference of target branch for the commit. Branch needs to already
              exist. For more information, see
              "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
              in the Git documentation.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix/commits",
            body=maybe_transform(
                {
                    "message": message,
                    "target_ref": target_ref,
                },
                autofix_commit_params.AutofixCommitParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AutofixCommitResponse,
        )


class AsyncAutofixResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutofixResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutofixResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutofixResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAutofixResourceWithStreamingResponse(self)

    async def create(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningAutofix:
        """
        Creates an autofix for a code scanning alert.

        If a new autofix is to be created as a result of this request or is currently
        being generated, then this endpoint will return a 202 Accepted response.

        If an autofix already exists for a given alert, then this endpoint will return a
        200 OK response.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningAutofix,
        )

    async def retrieve(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningAutofix:
        """
        Gets the status and description of an autofix for a code scanning alert.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningAutofix,
        )

    async def commit(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        message: str | NotGiven = NOT_GIVEN,
        target_ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutofixCommitResponse:
        """
        Commits an autofix for a code scanning alert.

        If an autofix is committed as a result of this request, then this endpoint will
        return a 201 Created response.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

          message: Commit message to be used.

          target_ref: The Git reference of target branch for the commit. Branch needs to already
              exist. For more information, see
              "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
              in the Git documentation.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix/commits",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "target_ref": target_ref,
                },
                autofix_commit_params.AutofixCommitParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AutofixCommitResponse,
        )


class AutofixResourceWithRawResponse:
    def __init__(self, autofix: AutofixResource) -> None:
        self._autofix = autofix

        self.create = to_raw_response_wrapper(
            autofix.create,
        )
        self.retrieve = to_raw_response_wrapper(
            autofix.retrieve,
        )
        self.commit = to_raw_response_wrapper(
            autofix.commit,
        )


class AsyncAutofixResourceWithRawResponse:
    def __init__(self, autofix: AsyncAutofixResource) -> None:
        self._autofix = autofix

        self.create = async_to_raw_response_wrapper(
            autofix.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            autofix.retrieve,
        )
        self.commit = async_to_raw_response_wrapper(
            autofix.commit,
        )


class AutofixResourceWithStreamingResponse:
    def __init__(self, autofix: AutofixResource) -> None:
        self._autofix = autofix

        self.create = to_streamed_response_wrapper(
            autofix.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            autofix.retrieve,
        )
        self.commit = to_streamed_response_wrapper(
            autofix.commit,
        )


class AsyncAutofixResourceWithStreamingResponse:
    def __init__(self, autofix: AsyncAutofixResource) -> None:
        self._autofix = autofix

        self.create = async_to_streamed_response_wrapper(
            autofix.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            autofix.retrieve,
        )
        self.commit = async_to_streamed_response_wrapper(
            autofix.commit,
        )
