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
from .....types.orgs.actions.secrets import repository_list_params, repository_set_params
from .....types.orgs.actions.secrets.repository_list_response import RepositoryListResponse

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
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryListResponse:
        """
        Lists all repositories that have been selected when the `visibility` for
        repository access to a secret is set to `selected`.

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._get(
            f"/orgs/{org}/actions/secrets/{secret_name}/repositories",
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
                    repository_list_params.RepositoryListParams,
                ),
            ),
            cast_to=RepositoryListResponse,
        )

    def add(
        self,
        repository_id: int,
        *,
        org: str,
        secret_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Adds a repository to an organization secret when the `visibility` for repository
        access is set to `selected`. For more information about setting the visibility,
        see
        [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def remove(
        self,
        repository_id: int,
        *,
        org: str,
        secret_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes a repository from an organization secret when the `visibility` for
        repository access is set to `selected`. The visibility is set when you
        [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def set(
        self,
        secret_name: str,
        *,
        org: str,
        selected_repository_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Replaces all repositories for an organization secret when the `visibility` for
        repository access is set to `selected`. The visibility is set when you
        [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          selected_repository_ids: An array of repository ids that can access the organization secret. You can only
              provide a list of repository ids when the `visibility` is set to `selected`. You
              can add and remove individual repositories using the
              [Add selected repository to an organization secret](https://docs.github.com/rest/actions/secrets#add-selected-repository-to-an-organization-secret)
              and
              [Remove selected repository from an organization secret](https://docs.github.com/rest/actions/secrets#remove-selected-repository-from-an-organization-secret)
              endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/orgs/{org}/actions/secrets/{secret_name}/repositories",
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
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryListResponse:
        """
        Lists all repositories that have been selected when the `visibility` for
        repository access to a secret is set to `selected`.

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._get(
            f"/orgs/{org}/actions/secrets/{secret_name}/repositories",
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
                    repository_list_params.RepositoryListParams,
                ),
            ),
            cast_to=RepositoryListResponse,
        )

    async def add(
        self,
        repository_id: int,
        *,
        org: str,
        secret_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Adds a repository to an organization secret when the `visibility` for repository
        access is set to `selected`. For more information about setting the visibility,
        see
        [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def remove(
        self,
        repository_id: int,
        *,
        org: str,
        secret_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes a repository from an organization secret when the `visibility` for
        repository access is set to `selected`. The visibility is set when you
        [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def set(
        self,
        secret_name: str,
        *,
        org: str,
        selected_repository_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Replaces all repositories for an organization secret when the `visibility` for
        repository access is set to `selected`. The visibility is set when you
        [Create or update an organization secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret).

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          selected_repository_ids: An array of repository ids that can access the organization secret. You can only
              provide a list of repository ids when the `visibility` is set to `selected`. You
              can add and remove individual repositories using the
              [Add selected repository to an organization secret](https://docs.github.com/rest/actions/secrets#add-selected-repository-to-an-organization-secret)
              and
              [Remove selected repository from an organization secret](https://docs.github.com/rest/actions/secrets#remove-selected-repository-from-an-organization-secret)
              endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/orgs/{org}/actions/secrets/{secret_name}/repositories",
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
