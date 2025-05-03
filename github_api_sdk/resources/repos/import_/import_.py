from __future__ import annotations

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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos import import_start_params, import_update_lfs_preferences_params, import_update_params
from ....types.repos.import_.import_ import Import
from ....types.repos.import_get_large_files_response import ImportGetLargeFilesResponse
from .authors import (
    AsyncAuthorsResource,
    AsyncAuthorsResourceWithRawResponse,
    AsyncAuthorsResourceWithStreamingResponse,
    AuthorsResource,
    AuthorsResourceWithRawResponse,
    AuthorsResourceWithStreamingResponse,
)

__all__ = ["ImportResource", "AsyncImportResource"]


class ImportResource(SyncAPIResource):
    @cached_property
    def authors(self) -> AuthorsResource:
        return AuthorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ImportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ImportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ImportResourceWithStreamingResponse(self)

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
    ) -> Import:
        """
        View the progress of an import.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        **Import status**

        This section includes details about the possible values of the `status` field of
        the Import Progress response.

        An import that does not have errors will progress through these steps:

        - `detecting` - the "detection" step of the import is in progress because the
          request did not include a `vcs` parameter. The import is identifying the type
          of source control present at the URL.
        - `importing` - the "raw" step of the import is in progress. This is where
          commit data is fetched from the original repository. The import progress
          response will include `commit_count` (the total number of raw commits that
          will be imported) and `percent` (0 - 100, the current progress through the
          import).
        - `mapping` - the "rewrite" step of the import is in progress. This is where SVN
          branches are converted to Git branches, and where author updates are applied.
          The import progress response does not include progress information.
        - `pushing` - the "push" step of the import is in progress. This is where the
          importer updates the repository on GitHub. The import progress response will
          include `push_percent`, which is the percent value reported by `git push` when
          it is "Writing objects".
        - `complete` - the import is complete, and the repository is ready on GitHub.

        If there are problems, you will see one of these in the `status` field:

        - `auth_failed` - the import requires authentication in order to connect to the
          original repository. To update authentication for the import, please see the
          [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import)
          section.
        - `error` - the import encountered an error. The import progress response will
          include the `failed_step` and an error message. Contact
          [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api) for
          more information.
        - `detection_needs_auth` - the importer requires authentication for the
          originating repository to continue detection. To update authentication for the
          import, please see the
          [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import)
          section.
        - `detection_found_nothing` - the importer didn't recognize any source control
          at the URL. To resolve,
          [Cancel the import](https://docs.github.com/rest/migrations/source-imports#cancel-an-import)
          and
          [retry](https://docs.github.com/rest/migrations/source-imports#start-an-import)
          with the correct URL.
        - `detection_found_multiple` - the importer found several projects or
          repositories at the provided URL. When this is the case, the Import Progress
          response will also include a `project_choices` field with the possible project
          choices as values. To update project choice, please see the
          [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import)
          section.

        **The project_choices field**

        When multiple projects are found at the provided URL, the response hash will
        include a `project_choices` field, the value of which is an array of hashes each
        representing a project choice. The exact key/value pairs of the project hashes
        will differ depending on the version control type.

        **Git LFS related fields**

        This section includes details about Git LFS related fields that may be present
        in the Import Progress response.

        - `use_lfs` - describes whether the import has been opted in or out of using Git
          LFS. The value can be `opt_in`, `opt_out`, or `undecided` if no action has
          been taken.
        - `has_large_files` - the boolean value describing whether files larger than
          100MB were found during the `importing` step.
        - `large_files_size` - the total size in gigabytes of files larger than 100MB
          found in the originating repository.
        - `large_files_count` - the total number of files larger than 100MB found in the
          originating repository. To see a list of these files, make a "Get Large Files"
          request.

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
            f"/repos/{owner}/{repo}/import",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Import,
        )

    def update(
        self,
        repo: str,
        *,
        owner: str,
        tfvc_project: str | NotGiven = NOT_GIVEN,
        vcs: Literal["subversion", "tfvc", "git", "mercurial"] | NotGiven = NOT_GIVEN,
        vcs_password: str | NotGiven = NOT_GIVEN,
        vcs_username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Import:
        """
        An import can be updated with credentials or a project choice by passing in the
        appropriate parameters in this API request. If no parameters are provided, the
        import will be restarted.

        Some servers (e.g. TFS servers) can have several projects at a single URL. In
        those cases the import progress will have the status `detection_found_multiple`
        and the Import Progress response will include a `project_choices` array. You can
        select the project to import by providing one of the objects in the
        `project_choices` array in the update request.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          tfvc_project: For a tfvc import, the name of the project that is being imported.

          vcs: The type of version control system you are migrating from.

          vcs_password: The password to provide to the originating repository.

          vcs_username: The username to provide to the originating repository.

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
            f"/repos/{owner}/{repo}/import",
            body=maybe_transform(
                {
                    "tfvc_project": tfvc_project,
                    "vcs": vcs,
                    "vcs_password": vcs_password,
                    "vcs_username": vcs_username,
                },
                import_update_params.ImportUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Import,
        )

    def cancel(
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
        """
        Stop an import for a repository.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

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
            f"/repos/{owner}/{repo}/import",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_large_files(
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
    ) -> ImportGetLargeFilesResponse:
        """
        List files larger than 100MB found during the import

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

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
            f"/repos/{owner}/{repo}/import/large_files",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ImportGetLargeFilesResponse,
        )

    def start(
        self,
        repo: str,
        *,
        owner: str,
        vcs_url: str,
        tfvc_project: str | NotGiven = NOT_GIVEN,
        vcs: Literal["subversion", "git", "mercurial", "tfvc"] | NotGiven = NOT_GIVEN,
        vcs_password: str | NotGiven = NOT_GIVEN,
        vcs_username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Import:
        """Start a source import to a GitHub repository using GitHub Importer.

        Importing
        into a GitHub repository with GitHub Actions enabled is not supported and will
        return a status `422 Unprocessable Entity` response.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          vcs_url: The URL of the originating repository.

          tfvc_project: For a tfvc import, the name of the project that is being imported.

          vcs: The originating VCS type. Without this parameter, the import job will take
              additional time to detect the VCS type before beginning the import. This
              detection step will be reflected in the response.

          vcs_password: If authentication is required, the password to provide to `vcs_url`.

          vcs_username: If authentication is required, the username to provide to `vcs_url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._put(
            f"/repos/{owner}/{repo}/import",
            body=maybe_transform(
                {
                    "vcs_url": vcs_url,
                    "tfvc_project": tfvc_project,
                    "vcs": vcs,
                    "vcs_password": vcs_password,
                    "vcs_username": vcs_username,
                },
                import_start_params.ImportStartParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Import,
        )

    def update_lfs_preferences(
        self,
        repo: str,
        *,
        owner: str,
        use_lfs: Literal["opt_in", "opt_out"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Import:
        """
        You can import repositories from Subversion, Mercurial, and TFS that include
        files larger than 100MB. This ability is powered by
        [Git LFS](https://git-lfs.com).

        You can learn more about our LFS feature and working with large files
        [on our help site](https://docs.github.com/repositories/working-with-files/managing-large-files).

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          use_lfs: Whether to store large files during the import. `opt_in` means large files will
              be stored using Git LFS. `opt_out` means large files will be removed during the
              import.

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
            f"/repos/{owner}/{repo}/import/lfs",
            body=maybe_transform({"use_lfs": use_lfs}, import_update_lfs_preferences_params.ImportUpdateLFSPreferencesParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Import,
        )


class AsyncImportResource(AsyncAPIResource):
    @cached_property
    def authors(self) -> AsyncAuthorsResource:
        return AsyncAuthorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncImportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncImportResourceWithStreamingResponse(self)

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
    ) -> Import:
        """
        View the progress of an import.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        **Import status**

        This section includes details about the possible values of the `status` field of
        the Import Progress response.

        An import that does not have errors will progress through these steps:

        - `detecting` - the "detection" step of the import is in progress because the
          request did not include a `vcs` parameter. The import is identifying the type
          of source control present at the URL.
        - `importing` - the "raw" step of the import is in progress. This is where
          commit data is fetched from the original repository. The import progress
          response will include `commit_count` (the total number of raw commits that
          will be imported) and `percent` (0 - 100, the current progress through the
          import).
        - `mapping` - the "rewrite" step of the import is in progress. This is where SVN
          branches are converted to Git branches, and where author updates are applied.
          The import progress response does not include progress information.
        - `pushing` - the "push" step of the import is in progress. This is where the
          importer updates the repository on GitHub. The import progress response will
          include `push_percent`, which is the percent value reported by `git push` when
          it is "Writing objects".
        - `complete` - the import is complete, and the repository is ready on GitHub.

        If there are problems, you will see one of these in the `status` field:

        - `auth_failed` - the import requires authentication in order to connect to the
          original repository. To update authentication for the import, please see the
          [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import)
          section.
        - `error` - the import encountered an error. The import progress response will
          include the `failed_step` and an error message. Contact
          [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api) for
          more information.
        - `detection_needs_auth` - the importer requires authentication for the
          originating repository to continue detection. To update authentication for the
          import, please see the
          [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import)
          section.
        - `detection_found_nothing` - the importer didn't recognize any source control
          at the URL. To resolve,
          [Cancel the import](https://docs.github.com/rest/migrations/source-imports#cancel-an-import)
          and
          [retry](https://docs.github.com/rest/migrations/source-imports#start-an-import)
          with the correct URL.
        - `detection_found_multiple` - the importer found several projects or
          repositories at the provided URL. When this is the case, the Import Progress
          response will also include a `project_choices` field with the possible project
          choices as values. To update project choice, please see the
          [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import)
          section.

        **The project_choices field**

        When multiple projects are found at the provided URL, the response hash will
        include a `project_choices` field, the value of which is an array of hashes each
        representing a project choice. The exact key/value pairs of the project hashes
        will differ depending on the version control type.

        **Git LFS related fields**

        This section includes details about Git LFS related fields that may be present
        in the Import Progress response.

        - `use_lfs` - describes whether the import has been opted in or out of using Git
          LFS. The value can be `opt_in`, `opt_out`, or `undecided` if no action has
          been taken.
        - `has_large_files` - the boolean value describing whether files larger than
          100MB were found during the `importing` step.
        - `large_files_size` - the total size in gigabytes of files larger than 100MB
          found in the originating repository.
        - `large_files_count` - the total number of files larger than 100MB found in the
          originating repository. To see a list of these files, make a "Get Large Files"
          request.

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
            f"/repos/{owner}/{repo}/import",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Import,
        )

    async def update(
        self,
        repo: str,
        *,
        owner: str,
        tfvc_project: str | NotGiven = NOT_GIVEN,
        vcs: Literal["subversion", "tfvc", "git", "mercurial"] | NotGiven = NOT_GIVEN,
        vcs_password: str | NotGiven = NOT_GIVEN,
        vcs_username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Import:
        """
        An import can be updated with credentials or a project choice by passing in the
        appropriate parameters in this API request. If no parameters are provided, the
        import will be restarted.

        Some servers (e.g. TFS servers) can have several projects at a single URL. In
        those cases the import progress will have the status `detection_found_multiple`
        and the Import Progress response will include a `project_choices` array. You can
        select the project to import by providing one of the objects in the
        `project_choices` array in the update request.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          tfvc_project: For a tfvc import, the name of the project that is being imported.

          vcs: The type of version control system you are migrating from.

          vcs_password: The password to provide to the originating repository.

          vcs_username: The username to provide to the originating repository.

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
            f"/repos/{owner}/{repo}/import",
            body=await async_maybe_transform(
                {
                    "tfvc_project": tfvc_project,
                    "vcs": vcs,
                    "vcs_password": vcs_password,
                    "vcs_username": vcs_username,
                },
                import_update_params.ImportUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Import,
        )

    async def cancel(
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
        """
        Stop an import for a repository.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

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
            f"/repos/{owner}/{repo}/import",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_large_files(
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
    ) -> ImportGetLargeFilesResponse:
        """
        List files larger than 100MB found during the import

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

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
            f"/repos/{owner}/{repo}/import/large_files",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ImportGetLargeFilesResponse,
        )

    async def start(
        self,
        repo: str,
        *,
        owner: str,
        vcs_url: str,
        tfvc_project: str | NotGiven = NOT_GIVEN,
        vcs: Literal["subversion", "git", "mercurial", "tfvc"] | NotGiven = NOT_GIVEN,
        vcs_password: str | NotGiven = NOT_GIVEN,
        vcs_username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Import:
        """Start a source import to a GitHub repository using GitHub Importer.

        Importing
        into a GitHub repository with GitHub Actions enabled is not supported and will
        return a status `422 Unprocessable Entity` response.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          vcs_url: The URL of the originating repository.

          tfvc_project: For a tfvc import, the name of the project that is being imported.

          vcs: The originating VCS type. Without this parameter, the import job will take
              additional time to detect the VCS type before beginning the import. This
              detection step will be reflected in the response.

          vcs_password: If authentication is required, the password to provide to `vcs_url`.

          vcs_username: If authentication is required, the username to provide to `vcs_url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/import",
            body=await async_maybe_transform(
                {
                    "vcs_url": vcs_url,
                    "tfvc_project": tfvc_project,
                    "vcs": vcs,
                    "vcs_password": vcs_password,
                    "vcs_username": vcs_username,
                },
                import_start_params.ImportStartParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Import,
        )

    async def update_lfs_preferences(
        self,
        repo: str,
        *,
        owner: str,
        use_lfs: Literal["opt_in", "opt_out"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Import:
        """
        You can import repositories from Subversion, Mercurial, and TFS that include
        files larger than 100MB. This ability is powered by
        [Git LFS](https://git-lfs.com).

        You can learn more about our LFS feature and working with large files
        [on our help site](https://docs.github.com/repositories/working-with-files/managing-large-files).

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          use_lfs: Whether to store large files during the import. `opt_in` means large files will
              be stored using Git LFS. `opt_out` means large files will be removed during the
              import.

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
            f"/repos/{owner}/{repo}/import/lfs",
            body=await async_maybe_transform({"use_lfs": use_lfs}, import_update_lfs_preferences_params.ImportUpdateLFSPreferencesParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Import,
        )


class ImportResourceWithRawResponse:
    def __init__(self, import_: ImportResource) -> None:
        self._import_ = import_

        self.retrieve = to_raw_response_wrapper(
            import_.retrieve,
        )
        self.update = to_raw_response_wrapper(
            import_.update,
        )
        self.cancel = to_raw_response_wrapper(
            import_.cancel,
        )
        self.get_large_files = to_raw_response_wrapper(
            import_.get_large_files,
        )
        self.start = to_raw_response_wrapper(
            import_.start,
        )
        self.update_lfs_preferences = to_raw_response_wrapper(
            import_.update_lfs_preferences,
        )

    @cached_property
    def authors(self) -> AuthorsResourceWithRawResponse:
        return AuthorsResourceWithRawResponse(self._import_.authors)


class AsyncImportResourceWithRawResponse:
    def __init__(self, import_: AsyncImportResource) -> None:
        self._import_ = import_

        self.retrieve = async_to_raw_response_wrapper(
            import_.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            import_.update,
        )
        self.cancel = async_to_raw_response_wrapper(
            import_.cancel,
        )
        self.get_large_files = async_to_raw_response_wrapper(
            import_.get_large_files,
        )
        self.start = async_to_raw_response_wrapper(
            import_.start,
        )
        self.update_lfs_preferences = async_to_raw_response_wrapper(
            import_.update_lfs_preferences,
        )

    @cached_property
    def authors(self) -> AsyncAuthorsResourceWithRawResponse:
        return AsyncAuthorsResourceWithRawResponse(self._import_.authors)


class ImportResourceWithStreamingResponse:
    def __init__(self, import_: ImportResource) -> None:
        self._import_ = import_

        self.retrieve = to_streamed_response_wrapper(
            import_.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            import_.update,
        )
        self.cancel = to_streamed_response_wrapper(
            import_.cancel,
        )
        self.get_large_files = to_streamed_response_wrapper(
            import_.get_large_files,
        )
        self.start = to_streamed_response_wrapper(
            import_.start,
        )
        self.update_lfs_preferences = to_streamed_response_wrapper(
            import_.update_lfs_preferences,
        )

    @cached_property
    def authors(self) -> AuthorsResourceWithStreamingResponse:
        return AuthorsResourceWithStreamingResponse(self._import_.authors)


class AsyncImportResourceWithStreamingResponse:
    def __init__(self, import_: AsyncImportResource) -> None:
        self._import_ = import_

        self.retrieve = async_to_streamed_response_wrapper(
            import_.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            import_.update,
        )
        self.cancel = async_to_streamed_response_wrapper(
            import_.cancel,
        )
        self.get_large_files = async_to_streamed_response_wrapper(
            import_.get_large_files,
        )
        self.start = async_to_streamed_response_wrapper(
            import_.start,
        )
        self.update_lfs_preferences = async_to_streamed_response_wrapper(
            import_.update_lfs_preferences,
        )

    @cached_property
    def authors(self) -> AsyncAuthorsResourceWithStreamingResponse:
        return AsyncAuthorsResourceWithStreamingResponse(self._import_.authors)
