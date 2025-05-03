from __future__ import annotations

import builtins
from typing import List

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
from ....._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs.actions.authentication_token import AuthenticationToken
from .....types.orgs.actions.self_hosted_runner import SelfHostedRunner
from .....types.repos.actions import runner_generate_jitconfig_params, runner_list_params
from .....types.repos.actions.runner_generate_jitconfig_response import RunnerGenerateJitconfigResponse
from .....types.repos.actions.runner_list_downloads_response import RunnerListDownloadsResponse
from .....types.repos.actions.runner_list_response import RunnerListResponse
from .labels import (
    AsyncLabelsResource,
    AsyncLabelsResourceWithRawResponse,
    AsyncLabelsResourceWithStreamingResponse,
    LabelsResource,
    LabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
)

__all__ = ["RunnersResource", "AsyncRunnersResource"]


class RunnersResource(SyncAPIResource):
    @cached_property
    def labels(self) -> LabelsResource:
        return LabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RunnersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        runner_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedRunner:
        """
        Gets a specific self-hosted runner configured in a repository.

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/actions/runners/{runner_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SelfHostedRunner,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerListResponse:
        """
        Lists all self-hosted runners configured in a repository.

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          name: The name of a self-hosted runner.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

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
            f"/repos/{owner}/{repo}/actions/runners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    runner_list_params.RunnerListParams,
                ),
            ),
            cast_to=RunnerListResponse,
        )

    def delete(
        self,
        runner_id: int,
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
        """Forces the removal of a self-hosted runner from a repository.

        You can use this
        endpoint to completely remove the runner when the machine you were using no
        longer exists.

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
            f"/repos/{owner}/{repo}/actions/runners/{runner_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_registration_token(
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
    ) -> AuthenticationToken:
        """Returns a token that you can pass to the `config` script.

        The token expires
        after one hour.

        For example, you can replace `TOKEN` in the following example with the
        registration token provided by this endpoint to configure your self-hosted
        runner:

        ```
        ./config.sh --url https://github.com/octo-org --token TOKEN
        ```

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return self._post(
            f"/repos/{owner}/{repo}/actions/runners/registration-token",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AuthenticationToken,
        )

    def create_remove_token(
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
    ) -> AuthenticationToken:
        """
        Returns a token that you can pass to the `config` script to remove a self-hosted
        runner from an repository. The token expires after one hour.

        For example, you can replace `TOKEN` in the following example with the
        registration token provided by this endpoint to remove your self-hosted runner
        from an organization:

        ```
        ./config.sh remove --token TOKEN
        ```

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return self._post(
            f"/repos/{owner}/{repo}/actions/runners/remove-token",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AuthenticationToken,
        )

    def generate_jitconfig(
        self,
        repo: str,
        *,
        owner: str,
        labels: builtins.list[str],
        name: str,
        runner_group_id: int,
        work_folder: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerGenerateJitconfigResponse:
        """
        Generates a configuration that can be passed to the runner application at
        startup.

        The authenticated user must have admin access to the repository.

        OAuth tokens and personal access tokens (classic) need the`repo` scope to use
        this endpoint.

        Args:
          labels: The names of the custom labels to add to the runner. **Minimum items**: 1.
              **Maximum items**: 100.

          name: The name of the new runner.

          runner_group_id: The ID of the runner group to register the runner to.

          work_folder: The working directory to be used for job execution, relative to the runner
              install directory.

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
            f"/repos/{owner}/{repo}/actions/runners/generate-jitconfig",
            body=maybe_transform(
                {
                    "labels": labels,
                    "name": name,
                    "runner_group_id": runner_group_id,
                    "work_folder": work_folder,
                },
                runner_generate_jitconfig_params.RunnerGenerateJitconfigParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RunnerGenerateJitconfigResponse,
        )

    def list_downloads(
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
    ) -> RunnerListDownloadsResponse:
        """
        Lists binaries for the runner application that you can download and run.

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/actions/runners/downloads",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RunnerListDownloadsResponse,
        )


class AsyncRunnersResource(AsyncAPIResource):
    @cached_property
    def labels(self) -> AsyncLabelsResource:
        return AsyncLabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRunnersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        runner_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelfHostedRunner:
        """
        Gets a specific self-hosted runner configured in a repository.

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/actions/runners/{runner_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SelfHostedRunner,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerListResponse:
        """
        Lists all self-hosted runners configured in a repository.

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          name: The name of a self-hosted runner.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

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
            f"/repos/{owner}/{repo}/actions/runners",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    runner_list_params.RunnerListParams,
                ),
            ),
            cast_to=RunnerListResponse,
        )

    async def delete(
        self,
        runner_id: int,
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
        """Forces the removal of a self-hosted runner from a repository.

        You can use this
        endpoint to completely remove the runner when the machine you were using no
        longer exists.

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
            f"/repos/{owner}/{repo}/actions/runners/{runner_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_registration_token(
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
    ) -> AuthenticationToken:
        """Returns a token that you can pass to the `config` script.

        The token expires
        after one hour.

        For example, you can replace `TOKEN` in the following example with the
        registration token provided by this endpoint to configure your self-hosted
        runner:

        ```
        ./config.sh --url https://github.com/octo-org --token TOKEN
        ```

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return await self._post(
            f"/repos/{owner}/{repo}/actions/runners/registration-token",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AuthenticationToken,
        )

    async def create_remove_token(
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
    ) -> AuthenticationToken:
        """
        Returns a token that you can pass to the `config` script to remove a self-hosted
        runner from an repository. The token expires after one hour.

        For example, you can replace `TOKEN` in the following example with the
        registration token provided by this endpoint to remove your self-hosted runner
        from an organization:

        ```
        ./config.sh remove --token TOKEN
        ```

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return await self._post(
            f"/repos/{owner}/{repo}/actions/runners/remove-token",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AuthenticationToken,
        )

    async def generate_jitconfig(
        self,
        repo: str,
        *,
        owner: str,
        labels: builtins.list[str],
        name: str,
        runner_group_id: int,
        work_folder: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerGenerateJitconfigResponse:
        """
        Generates a configuration that can be passed to the runner application at
        startup.

        The authenticated user must have admin access to the repository.

        OAuth tokens and personal access tokens (classic) need the`repo` scope to use
        this endpoint.

        Args:
          labels: The names of the custom labels to add to the runner. **Minimum items**: 1.
              **Maximum items**: 100.

          name: The name of the new runner.

          runner_group_id: The ID of the runner group to register the runner to.

          work_folder: The working directory to be used for job execution, relative to the runner
              install directory.

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
            f"/repos/{owner}/{repo}/actions/runners/generate-jitconfig",
            body=await async_maybe_transform(
                {
                    "labels": labels,
                    "name": name,
                    "runner_group_id": runner_group_id,
                    "work_folder": work_folder,
                },
                runner_generate_jitconfig_params.RunnerGenerateJitconfigParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RunnerGenerateJitconfigResponse,
        )

    async def list_downloads(
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
    ) -> RunnerListDownloadsResponse:
        """
        Lists binaries for the runner application that you can download and run.

        Authenticated users must have admin access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/actions/runners/downloads",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RunnerListDownloadsResponse,
        )


class RunnersResourceWithRawResponse:
    def __init__(self, runners: RunnersResource) -> None:
        self._runners = runners

        self.retrieve = to_raw_response_wrapper(
            runners.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runners.list,
        )
        self.delete = to_raw_response_wrapper(
            runners.delete,
        )
        self.create_registration_token = to_raw_response_wrapper(
            runners.create_registration_token,
        )
        self.create_remove_token = to_raw_response_wrapper(
            runners.create_remove_token,
        )
        self.generate_jitconfig = to_raw_response_wrapper(
            runners.generate_jitconfig,
        )
        self.list_downloads = to_raw_response_wrapper(
            runners.list_downloads,
        )

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        return LabelsResourceWithRawResponse(self._runners.labels)


class AsyncRunnersResourceWithRawResponse:
    def __init__(self, runners: AsyncRunnersResource) -> None:
        self._runners = runners

        self.retrieve = async_to_raw_response_wrapper(
            runners.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runners.list,
        )
        self.delete = async_to_raw_response_wrapper(
            runners.delete,
        )
        self.create_registration_token = async_to_raw_response_wrapper(
            runners.create_registration_token,
        )
        self.create_remove_token = async_to_raw_response_wrapper(
            runners.create_remove_token,
        )
        self.generate_jitconfig = async_to_raw_response_wrapper(
            runners.generate_jitconfig,
        )
        self.list_downloads = async_to_raw_response_wrapper(
            runners.list_downloads,
        )

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        return AsyncLabelsResourceWithRawResponse(self._runners.labels)


class RunnersResourceWithStreamingResponse:
    def __init__(self, runners: RunnersResource) -> None:
        self._runners = runners

        self.retrieve = to_streamed_response_wrapper(
            runners.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runners.list,
        )
        self.delete = to_streamed_response_wrapper(
            runners.delete,
        )
        self.create_registration_token = to_streamed_response_wrapper(
            runners.create_registration_token,
        )
        self.create_remove_token = to_streamed_response_wrapper(
            runners.create_remove_token,
        )
        self.generate_jitconfig = to_streamed_response_wrapper(
            runners.generate_jitconfig,
        )
        self.list_downloads = to_streamed_response_wrapper(
            runners.list_downloads,
        )

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        return LabelsResourceWithStreamingResponse(self._runners.labels)


class AsyncRunnersResourceWithStreamingResponse:
    def __init__(self, runners: AsyncRunnersResource) -> None:
        self._runners = runners

        self.retrieve = async_to_streamed_response_wrapper(
            runners.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runners.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            runners.delete,
        )
        self.create_registration_token = async_to_streamed_response_wrapper(
            runners.create_registration_token,
        )
        self.create_remove_token = async_to_streamed_response_wrapper(
            runners.create_remove_token,
        )
        self.generate_jitconfig = async_to_streamed_response_wrapper(
            runners.generate_jitconfig,
        )
        self.list_downloads = async_to_streamed_response_wrapper(
            runners.list_downloads,
        )

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        return AsyncLabelsResourceWithStreamingResponse(self._runners.labels)
