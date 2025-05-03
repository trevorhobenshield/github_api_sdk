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
from ...types.repos.automated_security_fix_check_response import AutomatedSecurityFixCheckResponse

__all__ = ["AutomatedSecurityFixesResource", "AsyncAutomatedSecurityFixesResource"]


class AutomatedSecurityFixesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomatedSecurityFixesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AutomatedSecurityFixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomatedSecurityFixesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AutomatedSecurityFixesResourceWithStreamingResponse(self)

    def check(
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
    ) -> AutomatedSecurityFixCheckResponse:
        """
        Shows whether Dependabot security updates are enabled, disabled or paused for a
        repository. The authenticated user must have admin read access to the
        repository. For more information, see
        "[Configuring Dependabot security updates](https://docs.github.com/articles/configuring-automated-security-fixes)".

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
            f"/repos/{owner}/{repo}/automated-security-fixes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AutomatedSecurityFixCheckResponse,
        )

    def disable(
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
    ) -> None:
        """Disables Dependabot security updates for a repository.

        The authenticated user
        must have admin access to the repository. For more information, see
        "[Configuring Dependabot security updates](https://docs.github.com/articles/configuring-automated-security-fixes)".

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
            f"/repos/{owner}/{repo}/automated-security-fixes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def enable(
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
    ) -> None:
        """Enables Dependabot security updates for a repository.

        The authenticated user
        must have admin access to the repository. For more information, see
        "[Configuring Dependabot security updates](https://docs.github.com/articles/configuring-automated-security-fixes)".

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
        return self._put(
            f"/repos/{owner}/{repo}/automated-security-fixes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncAutomatedSecurityFixesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomatedSecurityFixesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutomatedSecurityFixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomatedSecurityFixesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAutomatedSecurityFixesResourceWithStreamingResponse(self)

    async def check(
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
    ) -> AutomatedSecurityFixCheckResponse:
        """
        Shows whether Dependabot security updates are enabled, disabled or paused for a
        repository. The authenticated user must have admin read access to the
        repository. For more information, see
        "[Configuring Dependabot security updates](https://docs.github.com/articles/configuring-automated-security-fixes)".

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
            f"/repos/{owner}/{repo}/automated-security-fixes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AutomatedSecurityFixCheckResponse,
        )

    async def disable(
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
    ) -> None:
        """Disables Dependabot security updates for a repository.

        The authenticated user
        must have admin access to the repository. For more information, see
        "[Configuring Dependabot security updates](https://docs.github.com/articles/configuring-automated-security-fixes)".

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
            f"/repos/{owner}/{repo}/automated-security-fixes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def enable(
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
    ) -> None:
        """Enables Dependabot security updates for a repository.

        The authenticated user
        must have admin access to the repository. For more information, see
        "[Configuring Dependabot security updates](https://docs.github.com/articles/configuring-automated-security-fixes)".

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
        return await self._put(
            f"/repos/{owner}/{repo}/automated-security-fixes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AutomatedSecurityFixesResourceWithRawResponse:
    def __init__(self, automated_security_fixes: AutomatedSecurityFixesResource) -> None:
        self._automated_security_fixes = automated_security_fixes

        self.check = to_raw_response_wrapper(
            automated_security_fixes.check,
        )
        self.disable = to_raw_response_wrapper(
            automated_security_fixes.disable,
        )
        self.enable = to_raw_response_wrapper(
            automated_security_fixes.enable,
        )


class AsyncAutomatedSecurityFixesResourceWithRawResponse:
    def __init__(self, automated_security_fixes: AsyncAutomatedSecurityFixesResource) -> None:
        self._automated_security_fixes = automated_security_fixes

        self.check = async_to_raw_response_wrapper(
            automated_security_fixes.check,
        )
        self.disable = async_to_raw_response_wrapper(
            automated_security_fixes.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            automated_security_fixes.enable,
        )


class AutomatedSecurityFixesResourceWithStreamingResponse:
    def __init__(self, automated_security_fixes: AutomatedSecurityFixesResource) -> None:
        self._automated_security_fixes = automated_security_fixes

        self.check = to_streamed_response_wrapper(
            automated_security_fixes.check,
        )
        self.disable = to_streamed_response_wrapper(
            automated_security_fixes.disable,
        )
        self.enable = to_streamed_response_wrapper(
            automated_security_fixes.enable,
        )


class AsyncAutomatedSecurityFixesResourceWithStreamingResponse:
    def __init__(self, automated_security_fixes: AsyncAutomatedSecurityFixesResource) -> None:
        self._automated_security_fixes = automated_security_fixes

        self.check = async_to_streamed_response_wrapper(
            automated_security_fixes.check,
        )
        self.disable = async_to_streamed_response_wrapper(
            automated_security_fixes.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            automated_security_fixes.enable,
        )
