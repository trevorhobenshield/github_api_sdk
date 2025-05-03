from __future__ import annotations

import builtins
from typing import List

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
from ....types.orgs import (
    migration_list_params,
    migration_list_repositories_params,
    migration_retrieve_status_params,
    migration_start_params,
)
from ....types.orgs.migration import Migration
from ....types.orgs.migration_list_repositories_response import MigrationListRepositoriesResponse
from ....types.orgs.migration_list_response import MigrationListResponse
from .archive import (
    ArchiveResource,
    ArchiveResourceWithRawResponse,
    ArchiveResourceWithStreamingResponse,
    AsyncArchiveResource,
    AsyncArchiveResourceWithRawResponse,
    AsyncArchiveResourceWithStreamingResponse,
)
from .repos import (
    AsyncReposResource,
    AsyncReposResourceWithRawResponse,
    AsyncReposResourceWithStreamingResponse,
    ReposResource,
    ReposResourceWithRawResponse,
    ReposResourceWithStreamingResponse,
)

__all__ = ["MigrationsResource", "AsyncMigrationsResource"]


class MigrationsResource(SyncAPIResource):
    @cached_property
    def archive(self) -> ArchiveResource:
        return ArchiveResource(self._client)

    @cached_property
    def repos(self) -> ReposResource:
        return ReposResource(self._client)

    @cached_property
    def with_raw_response(self) -> MigrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MigrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MigrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MigrationsResourceWithStreamingResponse(self)

    def list(
        self,
        org: str,
        *,
        exclude: builtins.list[Literal["repositories"]] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationListResponse:
        """
        Lists the most recent migrations, including both exports (which can be started
        through the REST API) and imports (which cannot be started using the REST API).

        A list of `repositories` is only returned for export migrations.

        Args:
          exclude: Exclude attributes from the API response to improve performance

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
        return self._get(
            f"/orgs/{org}/migrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude": exclude,
                        "page": page,
                        "per_page": per_page,
                    },
                    migration_list_params.MigrationListParams,
                ),
            ),
            cast_to=MigrationListResponse,
        )

    def list_repositories(
        self,
        migration_id: int,
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
    ) -> MigrationListRepositoriesResponse:
        """
        List all the repositories for this organization migration.

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
        return self._get(
            f"/orgs/{org}/migrations/{migration_id}/repositories",
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
                    migration_list_repositories_params.MigrationListRepositoriesParams,
                ),
            ),
            cast_to=MigrationListRepositoriesResponse,
        )

    def retrieve_status(
        self,
        migration_id: int,
        *,
        org: str,
        exclude: builtins.list[Literal["repositories"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Migration:
        """
        Fetches the status of a migration.

        The `state` of a migration can be one of the following values:

        - `pending`, which means the migration hasn't started yet.
        - `exporting`, which means the migration is in progress.
        - `exported`, which means the migration finished successfully.
        - `failed`, which means the migration failed.

        Args:
          exclude: Exclude attributes from the API response to improve performance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/migrations/{migration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"exclude": exclude}, migration_retrieve_status_params.MigrationRetrieveStatusParams),
            ),
            cast_to=Migration,
        )

    def start(
        self,
        org: str,
        *,
        repositories: builtins.list[str],
        exclude: builtins.list[Literal["repositories"]] | NotGiven = NOT_GIVEN,
        exclude_attachments: bool | NotGiven = NOT_GIVEN,
        exclude_git_data: bool | NotGiven = NOT_GIVEN,
        exclude_metadata: bool | NotGiven = NOT_GIVEN,
        exclude_owner_projects: bool | NotGiven = NOT_GIVEN,
        exclude_releases: bool | NotGiven = NOT_GIVEN,
        lock_repositories: bool | NotGiven = NOT_GIVEN,
        org_metadata_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Migration:
        """
        Initiates the generation of a migration archive.

        Args:
          repositories: A list of arrays indicating which repositories should be migrated.

          exclude: Exclude related items from being returned in the response in order to improve
              performance of the request.

          exclude_attachments: Indicates whether attachments should be excluded from the migration (to reduce
              migration archive file size).

          exclude_git_data: Indicates whether the repository git data should be excluded from the migration.

          exclude_metadata: Indicates whether metadata should be excluded and only git source should be
              included for the migration.

          exclude_owner_projects: Indicates whether projects owned by the organization or users should be
              excluded. from the migration.

          exclude_releases: Indicates whether releases should be excluded from the migration (to reduce
              migration archive file size).

          lock_repositories: Indicates whether repositories should be locked (to prevent manipulation) while
              migrating data.

          org_metadata_only: Indicates whether this should only include organization metadata (repositories
              array should be empty and will ignore other flags).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/migrations",
            body=maybe_transform(
                {
                    "repositories": repositories,
                    "exclude": exclude,
                    "exclude_attachments": exclude_attachments,
                    "exclude_git_data": exclude_git_data,
                    "exclude_metadata": exclude_metadata,
                    "exclude_owner_projects": exclude_owner_projects,
                    "exclude_releases": exclude_releases,
                    "lock_repositories": lock_repositories,
                    "org_metadata_only": org_metadata_only,
                },
                migration_start_params.MigrationStartParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Migration,
        )


class AsyncMigrationsResource(AsyncAPIResource):
    @cached_property
    def archive(self) -> AsyncArchiveResource:
        return AsyncArchiveResource(self._client)

    @cached_property
    def repos(self) -> AsyncReposResource:
        return AsyncReposResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMigrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMigrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMigrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMigrationsResourceWithStreamingResponse(self)

    async def list(
        self,
        org: str,
        *,
        exclude: builtins.list[Literal["repositories"]] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationListResponse:
        """
        Lists the most recent migrations, including both exports (which can be started
        through the REST API) and imports (which cannot be started using the REST API).

        A list of `repositories` is only returned for export migrations.

        Args:
          exclude: Exclude attributes from the API response to improve performance

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
        return await self._get(
            f"/orgs/{org}/migrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude": exclude,
                        "page": page,
                        "per_page": per_page,
                    },
                    migration_list_params.MigrationListParams,
                ),
            ),
            cast_to=MigrationListResponse,
        )

    async def list_repositories(
        self,
        migration_id: int,
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
    ) -> MigrationListRepositoriesResponse:
        """
        List all the repositories for this organization migration.

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
        return await self._get(
            f"/orgs/{org}/migrations/{migration_id}/repositories",
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
                    migration_list_repositories_params.MigrationListRepositoriesParams,
                ),
            ),
            cast_to=MigrationListRepositoriesResponse,
        )

    async def retrieve_status(
        self,
        migration_id: int,
        *,
        org: str,
        exclude: builtins.list[Literal["repositories"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Migration:
        """
        Fetches the status of a migration.

        The `state` of a migration can be one of the following values:

        - `pending`, which means the migration hasn't started yet.
        - `exporting`, which means the migration is in progress.
        - `exported`, which means the migration finished successfully.
        - `failed`, which means the migration failed.

        Args:
          exclude: Exclude attributes from the API response to improve performance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/migrations/{migration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"exclude": exclude}, migration_retrieve_status_params.MigrationRetrieveStatusParams),
            ),
            cast_to=Migration,
        )

    async def start(
        self,
        org: str,
        *,
        repositories: builtins.list[str],
        exclude: builtins.list[Literal["repositories"]] | NotGiven = NOT_GIVEN,
        exclude_attachments: bool | NotGiven = NOT_GIVEN,
        exclude_git_data: bool | NotGiven = NOT_GIVEN,
        exclude_metadata: bool | NotGiven = NOT_GIVEN,
        exclude_owner_projects: bool | NotGiven = NOT_GIVEN,
        exclude_releases: bool | NotGiven = NOT_GIVEN,
        lock_repositories: bool | NotGiven = NOT_GIVEN,
        org_metadata_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Migration:
        """
        Initiates the generation of a migration archive.

        Args:
          repositories: A list of arrays indicating which repositories should be migrated.

          exclude: Exclude related items from being returned in the response in order to improve
              performance of the request.

          exclude_attachments: Indicates whether attachments should be excluded from the migration (to reduce
              migration archive file size).

          exclude_git_data: Indicates whether the repository git data should be excluded from the migration.

          exclude_metadata: Indicates whether metadata should be excluded and only git source should be
              included for the migration.

          exclude_owner_projects: Indicates whether projects owned by the organization or users should be
              excluded. from the migration.

          exclude_releases: Indicates whether releases should be excluded from the migration (to reduce
              migration archive file size).

          lock_repositories: Indicates whether repositories should be locked (to prevent manipulation) while
              migrating data.

          org_metadata_only: Indicates whether this should only include organization metadata (repositories
              array should be empty and will ignore other flags).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/migrations",
            body=await async_maybe_transform(
                {
                    "repositories": repositories,
                    "exclude": exclude,
                    "exclude_attachments": exclude_attachments,
                    "exclude_git_data": exclude_git_data,
                    "exclude_metadata": exclude_metadata,
                    "exclude_owner_projects": exclude_owner_projects,
                    "exclude_releases": exclude_releases,
                    "lock_repositories": lock_repositories,
                    "org_metadata_only": org_metadata_only,
                },
                migration_start_params.MigrationStartParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Migration,
        )


class MigrationsResourceWithRawResponse:
    def __init__(self, migrations: MigrationsResource) -> None:
        self._migrations = migrations

        self.list = to_raw_response_wrapper(
            migrations.list,
        )
        self.list_repositories = to_raw_response_wrapper(
            migrations.list_repositories,
        )
        self.retrieve_status = to_raw_response_wrapper(
            migrations.retrieve_status,
        )
        self.start = to_raw_response_wrapper(
            migrations.start,
        )

    @cached_property
    def archive(self) -> ArchiveResourceWithRawResponse:
        return ArchiveResourceWithRawResponse(self._migrations.archive)

    @cached_property
    def repos(self) -> ReposResourceWithRawResponse:
        return ReposResourceWithRawResponse(self._migrations.repos)


class AsyncMigrationsResourceWithRawResponse:
    def __init__(self, migrations: AsyncMigrationsResource) -> None:
        self._migrations = migrations

        self.list = async_to_raw_response_wrapper(
            migrations.list,
        )
        self.list_repositories = async_to_raw_response_wrapper(
            migrations.list_repositories,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            migrations.retrieve_status,
        )
        self.start = async_to_raw_response_wrapper(
            migrations.start,
        )

    @cached_property
    def archive(self) -> AsyncArchiveResourceWithRawResponse:
        return AsyncArchiveResourceWithRawResponse(self._migrations.archive)

    @cached_property
    def repos(self) -> AsyncReposResourceWithRawResponse:
        return AsyncReposResourceWithRawResponse(self._migrations.repos)


class MigrationsResourceWithStreamingResponse:
    def __init__(self, migrations: MigrationsResource) -> None:
        self._migrations = migrations

        self.list = to_streamed_response_wrapper(
            migrations.list,
        )
        self.list_repositories = to_streamed_response_wrapper(
            migrations.list_repositories,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            migrations.retrieve_status,
        )
        self.start = to_streamed_response_wrapper(
            migrations.start,
        )

    @cached_property
    def archive(self) -> ArchiveResourceWithStreamingResponse:
        return ArchiveResourceWithStreamingResponse(self._migrations.archive)

    @cached_property
    def repos(self) -> ReposResourceWithStreamingResponse:
        return ReposResourceWithStreamingResponse(self._migrations.repos)


class AsyncMigrationsResourceWithStreamingResponse:
    def __init__(self, migrations: AsyncMigrationsResource) -> None:
        self._migrations = migrations

        self.list = async_to_streamed_response_wrapper(
            migrations.list,
        )
        self.list_repositories = async_to_streamed_response_wrapper(
            migrations.list_repositories,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            migrations.retrieve_status,
        )
        self.start = async_to_streamed_response_wrapper(
            migrations.start,
        )

    @cached_property
    def archive(self) -> AsyncArchiveResourceWithStreamingResponse:
        return AsyncArchiveResourceWithStreamingResponse(self._migrations.archive)

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._migrations.repos)
