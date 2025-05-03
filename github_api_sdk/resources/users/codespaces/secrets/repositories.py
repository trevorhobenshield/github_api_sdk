from __future__ import annotations

from typing import Iterable

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
from .....types.users.codespaces.secrets import repository_set_params
from .....types.users.codespaces.secrets.repository_list_response import RepositoryListResponse

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
        secret_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryListResponse:
        """
        List the repositories that have been granted the ability to use a user's
        development environment secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._get(
            f"/user/codespaces/secrets/{secret_name}/repositories",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryListResponse,
        )

    def add(
        self,
        repository_id: int,
        *,
        secret_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Adds a repository to the selected repositories for a user's development
        environment secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/user/codespaces/secrets/{secret_name}/repositories/{repository_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def remove(
        self,
        repository_id: int,
        *,
        secret_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes a repository from the selected repositories for a user's development
        environment secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/user/codespaces/secrets/{secret_name}/repositories/{repository_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def set(
        self,
        secret_name: str,
        *,
        selected_repository_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Select the repositories that will use a user's development environment secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          selected_repository_ids: An array of repository ids for which a codespace can access the secret. You can
              manage the list of selected repositories using the
              [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret),
              [Add a selected repository to a user secret](https://docs.github.com/rest/codespaces/secrets#add-a-selected-repository-to-a-user-secret),
              and
              [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret)
              endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/user/codespaces/secrets/{secret_name}/repositories",
            body=maybe_transform({"selected_repository_ids": selected_repository_ids}, repository_set_params.RepositorySetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
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
        secret_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryListResponse:
        """
        List the repositories that have been granted the ability to use a user's
        development environment secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._get(
            f"/user/codespaces/secrets/{secret_name}/repositories",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryListResponse,
        )

    async def add(
        self,
        repository_id: int,
        *,
        secret_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Adds a repository to the selected repositories for a user's development
        environment secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/user/codespaces/secrets/{secret_name}/repositories/{repository_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def remove(
        self,
        repository_id: int,
        *,
        secret_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes a repository from the selected repositories for a user's development
        environment secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/user/codespaces/secrets/{secret_name}/repositories/{repository_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def set(
        self,
        secret_name: str,
        *,
        selected_repository_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Select the repositories that will use a user's development environment secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          selected_repository_ids: An array of repository ids for which a codespace can access the secret. You can
              manage the list of selected repositories using the
              [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret),
              [Add a selected repository to a user secret](https://docs.github.com/rest/codespaces/secrets#add-a-selected-repository-to-a-user-secret),
              and
              [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret)
              endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/user/codespaces/secrets/{secret_name}/repositories",
            body=await async_maybe_transform({"selected_repository_ids": selected_repository_ids}, repository_set_params.RepositorySetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class RepositoriesResourceWithRawResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.list = to_raw_response_wrapper(
            repositories.list,
        )
        self.add = to_raw_response_wrapper(
            repositories.add,
        )
        self.remove = to_raw_response_wrapper(
            repositories.remove,
        )
        self.set = to_raw_response_wrapper(
            repositories.set,
        )


class AsyncRepositoriesResourceWithRawResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.list = async_to_raw_response_wrapper(
            repositories.list,
        )
        self.add = async_to_raw_response_wrapper(
            repositories.add,
        )
        self.remove = async_to_raw_response_wrapper(
            repositories.remove,
        )
        self.set = async_to_raw_response_wrapper(
            repositories.set,
        )


class RepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: RepositoriesResource) -> None:
        self._repositories = repositories

        self.list = to_streamed_response_wrapper(
            repositories.list,
        )
        self.add = to_streamed_response_wrapper(
            repositories.add,
        )
        self.remove = to_streamed_response_wrapper(
            repositories.remove,
        )
        self.set = to_streamed_response_wrapper(
            repositories.set,
        )


class AsyncRepositoriesResourceWithStreamingResponse:
    def __init__(self, repositories: AsyncRepositoriesResource) -> None:
        self._repositories = repositories

        self.list = async_to_streamed_response_wrapper(
            repositories.list,
        )
        self.add = async_to_streamed_response_wrapper(
            repositories.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            repositories.remove,
        )
        self.set = async_to_streamed_response_wrapper(
            repositories.set,
        )
