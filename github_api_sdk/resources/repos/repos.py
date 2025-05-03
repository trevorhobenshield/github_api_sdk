from __future__ import annotations

from typing import Any, Dict, Iterable, Optional, cast

import httpx
from typing_extensions import Literal

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
from ...types import (
    repo_compare_commits_params,
    repo_create_commit_status_params,
    repo_create_dispatch_event_params,
    repo_create_from_template_params,
    repo_get_license_params,
    repo_list_activity_params,
    repo_list_contributors_params,
    repo_list_events_params,
    repo_list_stargazers_params,
    repo_list_teams_params,
    repo_list_watchers_params,
    repo_merge_branch_params,
    repo_sync_with_upstream_params,
    repo_transfer_params,
    repo_update_params,
)
from ...types.applications.installation import Installation
from ...types.minimal_repository import MinimalRepository
from ...types.orgs.full_repository import FullRepository
from ...types.repo_compare_commits_response import RepoCompareCommitsResponse
from ...types.repo_get_code_security_configuration_response import RepoGetCodeSecurityConfigurationResponse
from ...types.repo_get_license_response import RepoGetLicenseResponse
from ...types.repo_list_activity_response import RepoListActivityResponse
from ...types.repo_list_contributors_response import RepoListContributorsResponse
from ...types.repo_list_events_response import RepoListEventsResponse
from ...types.repo_list_languages_response import RepoListLanguagesResponse
from ...types.repo_list_stargazers_response import RepoListStargazersResponse
from ...types.repo_list_teams_response import RepoListTeamsResponse
from ...types.repo_list_watchers_response import RepoListWatchersResponse
from ...types.repo_sync_with_upstream_response import RepoSyncWithUpstreamResponse
from ...types.repos.commit import Commit
from ...types.status import Status
from .actions.actions import (
    ActionsResource,
    ActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResource,
    AsyncActionsResourceWithRawResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from .assignees import (
    AssigneesResource,
    AssigneesResourceWithRawResponse,
    AssigneesResourceWithStreamingResponse,
    AsyncAssigneesResource,
    AsyncAssigneesResourceWithRawResponse,
    AsyncAssigneesResourceWithStreamingResponse,
)
from .attestations import (
    AsyncAttestationsResource,
    AsyncAttestationsResourceWithRawResponse,
    AsyncAttestationsResourceWithStreamingResponse,
    AttestationsResource,
    AttestationsResourceWithRawResponse,
    AttestationsResourceWithStreamingResponse,
)
from .autolinks import (
    AsyncAutolinksResource,
    AsyncAutolinksResourceWithRawResponse,
    AsyncAutolinksResourceWithStreamingResponse,
    AutolinksResource,
    AutolinksResourceWithRawResponse,
    AutolinksResourceWithStreamingResponse,
)
from .automated_security_fixes import (
    AsyncAutomatedSecurityFixesResource,
    AsyncAutomatedSecurityFixesResourceWithRawResponse,
    AsyncAutomatedSecurityFixesResourceWithStreamingResponse,
    AutomatedSecurityFixesResource,
    AutomatedSecurityFixesResourceWithRawResponse,
    AutomatedSecurityFixesResourceWithStreamingResponse,
)
from .branches.branches import (
    AsyncBranchesResource,
    AsyncBranchesResourceWithRawResponse,
    AsyncBranchesResourceWithStreamingResponse,
    BranchesResource,
    BranchesResourceWithRawResponse,
    BranchesResourceWithStreamingResponse,
)
from .check_runs import (
    AsyncCheckRunsResource,
    AsyncCheckRunsResourceWithRawResponse,
    AsyncCheckRunsResourceWithStreamingResponse,
    CheckRunsResource,
    CheckRunsResourceWithRawResponse,
    CheckRunsResourceWithStreamingResponse,
)
from .check_suites import (
    AsyncCheckSuitesResource,
    AsyncCheckSuitesResourceWithRawResponse,
    AsyncCheckSuitesResourceWithStreamingResponse,
    CheckSuitesResource,
    CheckSuitesResourceWithRawResponse,
    CheckSuitesResourceWithStreamingResponse,
)
from .code_scanning.code_scanning import (
    AsyncCodeScanningResource,
    AsyncCodeScanningResourceWithRawResponse,
    AsyncCodeScanningResourceWithStreamingResponse,
    CodeScanningResource,
    CodeScanningResourceWithRawResponse,
    CodeScanningResourceWithStreamingResponse,
)
from .codeowners import (
    AsyncCodeownersResource,
    AsyncCodeownersResourceWithRawResponse,
    AsyncCodeownersResourceWithStreamingResponse,
    CodeownersResource,
    CodeownersResourceWithRawResponse,
    CodeownersResourceWithStreamingResponse,
)
from .codespaces.codespaces import (
    AsyncCodespacesResource,
    AsyncCodespacesResourceWithRawResponse,
    AsyncCodespacesResourceWithStreamingResponse,
    CodespacesResource,
    CodespacesResourceWithRawResponse,
    CodespacesResourceWithStreamingResponse,
)
from .collaborators import (
    AsyncCollaboratorsResource,
    AsyncCollaboratorsResourceWithRawResponse,
    AsyncCollaboratorsResourceWithStreamingResponse,
    CollaboratorsResource,
    CollaboratorsResourceWithRawResponse,
    CollaboratorsResourceWithStreamingResponse,
)
from .comments.comments import (
    AsyncCommentsResource,
    AsyncCommentsResourceWithRawResponse,
    AsyncCommentsResourceWithStreamingResponse,
    CommentsResource,
    CommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
)
from .commits.commits import (
    AsyncCommitsResource,
    AsyncCommitsResourceWithRawResponse,
    AsyncCommitsResourceWithStreamingResponse,
    CommitsResource,
    CommitsResourceWithRawResponse,
    CommitsResourceWithStreamingResponse,
)
from .community import (
    AsyncCommunityResource,
    AsyncCommunityResourceWithRawResponse,
    AsyncCommunityResourceWithStreamingResponse,
    CommunityResource,
    CommunityResourceWithRawResponse,
    CommunityResourceWithStreamingResponse,
)
from .contents import (
    AsyncContentsResource,
    AsyncContentsResourceWithRawResponse,
    AsyncContentsResourceWithStreamingResponse,
    ContentsResource,
    ContentsResourceWithRawResponse,
    ContentsResourceWithStreamingResponse,
)
from .dependabot.dependabot import (
    AsyncDependabotResource,
    AsyncDependabotResourceWithRawResponse,
    AsyncDependabotResourceWithStreamingResponse,
    DependabotResource,
    DependabotResourceWithRawResponse,
    DependabotResourceWithStreamingResponse,
)
from .dependency_graph import (
    AsyncDependencyGraphResource,
    AsyncDependencyGraphResourceWithRawResponse,
    AsyncDependencyGraphResourceWithStreamingResponse,
    DependencyGraphResource,
    DependencyGraphResourceWithRawResponse,
    DependencyGraphResourceWithStreamingResponse,
)
from .deployments.deployments import (
    AsyncDeploymentsResource,
    AsyncDeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
    DeploymentsResource,
    DeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
)
from .environments.environments import (
    AsyncEnvironmentsResource,
    AsyncEnvironmentsResourceWithRawResponse,
    AsyncEnvironmentsResourceWithStreamingResponse,
    EnvironmentsResource,
    EnvironmentsResourceWithRawResponse,
    EnvironmentsResourceWithStreamingResponse,
)
from .forks import (
    AsyncForksResource,
    AsyncForksResourceWithRawResponse,
    AsyncForksResourceWithStreamingResponse,
    ForksResource,
    ForksResourceWithRawResponse,
    ForksResourceWithStreamingResponse,
)
from .git.git import (
    AsyncGitResource,
    AsyncGitResourceWithRawResponse,
    AsyncGitResourceWithStreamingResponse,
    GitResource,
    GitResourceWithRawResponse,
    GitResourceWithStreamingResponse,
)
from .hooks.hooks import (
    AsyncHooksResource,
    AsyncHooksResourceWithRawResponse,
    AsyncHooksResourceWithStreamingResponse,
    HooksResource,
    HooksResourceWithRawResponse,
    HooksResourceWithStreamingResponse,
)
from .import_.import_ import (
    AsyncImportResource,
    AsyncImportResourceWithRawResponse,
    AsyncImportResourceWithStreamingResponse,
    ImportResource,
    ImportResourceWithRawResponse,
    ImportResourceWithStreamingResponse,
)
from .interaction_limits import (
    AsyncInteractionLimitsResource,
    AsyncInteractionLimitsResourceWithRawResponse,
    AsyncInteractionLimitsResourceWithStreamingResponse,
    InteractionLimitsResource,
    InteractionLimitsResourceWithRawResponse,
    InteractionLimitsResourceWithStreamingResponse,
)
from .invitations import (
    AsyncInvitationsResource,
    AsyncInvitationsResourceWithRawResponse,
    AsyncInvitationsResourceWithStreamingResponse,
    InvitationsResource,
    InvitationsResourceWithRawResponse,
    InvitationsResourceWithStreamingResponse,
)
from .issues.issues import (
    AsyncIssuesResource,
    AsyncIssuesResourceWithRawResponse,
    AsyncIssuesResourceWithStreamingResponse,
    IssuesResource,
    IssuesResourceWithRawResponse,
    IssuesResourceWithStreamingResponse,
)
from .keys import (
    AsyncKeysResource,
    AsyncKeysResourceWithRawResponse,
    AsyncKeysResourceWithStreamingResponse,
    KeysResource,
    KeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
)
from .labels import (
    AsyncLabelsResource,
    AsyncLabelsResourceWithRawResponse,
    AsyncLabelsResourceWithStreamingResponse,
    LabelsResource,
    LabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
)
from .milestones import (
    AsyncMilestonesResource,
    AsyncMilestonesResourceWithRawResponse,
    AsyncMilestonesResourceWithStreamingResponse,
    MilestonesResource,
    MilestonesResourceWithRawResponse,
    MilestonesResourceWithStreamingResponse,
)
from .notifications import (
    AsyncNotificationsResource,
    AsyncNotificationsResourceWithRawResponse,
    AsyncNotificationsResourceWithStreamingResponse,
    NotificationsResource,
    NotificationsResourceWithRawResponse,
    NotificationsResourceWithStreamingResponse,
)
from .pages.pages import (
    AsyncPagesResource,
    AsyncPagesResourceWithRawResponse,
    AsyncPagesResourceWithStreamingResponse,
    PagesResource,
    PagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
)
from .private_vulnerability_reporting import (
    AsyncPrivateVulnerabilityReportingResource,
    AsyncPrivateVulnerabilityReportingResourceWithRawResponse,
    AsyncPrivateVulnerabilityReportingResourceWithStreamingResponse,
    PrivateVulnerabilityReportingResource,
    PrivateVulnerabilityReportingResourceWithRawResponse,
    PrivateVulnerabilityReportingResourceWithStreamingResponse,
)
from .projects import (
    AsyncProjectsResource,
    AsyncProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithStreamingResponse,
    ProjectsResource,
    ProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
)
from .properties.properties import (
    AsyncPropertiesResource,
    AsyncPropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithStreamingResponse,
    PropertiesResource,
    PropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
)
from .pulls.pulls import (
    AsyncPullsResource,
    AsyncPullsResourceWithRawResponse,
    AsyncPullsResourceWithStreamingResponse,
    PullsResource,
    PullsResourceWithRawResponse,
    PullsResourceWithStreamingResponse,
)
from .readme import (
    AsyncReadmeResource,
    AsyncReadmeResourceWithRawResponse,
    AsyncReadmeResourceWithStreamingResponse,
    ReadmeResource,
    ReadmeResourceWithRawResponse,
    ReadmeResourceWithStreamingResponse,
)
from .releases.releases import (
    AsyncReleasesResource,
    AsyncReleasesResourceWithRawResponse,
    AsyncReleasesResourceWithStreamingResponse,
    ReleasesResource,
    ReleasesResourceWithRawResponse,
    ReleasesResourceWithStreamingResponse,
)
from .rules import (
    AsyncRulesResource,
    AsyncRulesResourceWithRawResponse,
    AsyncRulesResourceWithStreamingResponse,
    RulesResource,
    RulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
)
from .rulesets.rulesets import (
    AsyncRulesetsResource,
    AsyncRulesetsResourceWithRawResponse,
    AsyncRulesetsResourceWithStreamingResponse,
    RulesetsResource,
    RulesetsResourceWithRawResponse,
    RulesetsResourceWithStreamingResponse,
)
from .secret_scanning.secret_scanning import (
    AsyncSecretScanningResource,
    AsyncSecretScanningResourceWithRawResponse,
    AsyncSecretScanningResourceWithStreamingResponse,
    SecretScanningResource,
    SecretScanningResourceWithRawResponse,
    SecretScanningResourceWithStreamingResponse,
)
from .security_advisories import (
    AsyncSecurityAdvisoriesResource,
    AsyncSecurityAdvisoriesResourceWithRawResponse,
    AsyncSecurityAdvisoriesResourceWithStreamingResponse,
    SecurityAdvisoriesResource,
    SecurityAdvisoriesResourceWithRawResponse,
    SecurityAdvisoriesResourceWithStreamingResponse,
)
from .stats import (
    AsyncStatsResource,
    AsyncStatsResourceWithRawResponse,
    AsyncStatsResourceWithStreamingResponse,
    StatsResource,
    StatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
)
from .subscription import (
    AsyncSubscriptionResource,
    AsyncSubscriptionResourceWithRawResponse,
    AsyncSubscriptionResourceWithStreamingResponse,
    SubscriptionResource,
    SubscriptionResourceWithRawResponse,
    SubscriptionResourceWithStreamingResponse,
)
from .tags.tags import (
    AsyncTagsResource,
    AsyncTagsResourceWithRawResponse,
    AsyncTagsResourceWithStreamingResponse,
    TagsResource,
    TagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
)
from .topics import (
    AsyncTopicsResource,
    AsyncTopicsResourceWithRawResponse,
    AsyncTopicsResourceWithStreamingResponse,
    TopicsResource,
    TopicsResourceWithRawResponse,
    TopicsResourceWithStreamingResponse,
)
from .traffic.traffic import (
    AsyncTrafficResource,
    AsyncTrafficResourceWithRawResponse,
    AsyncTrafficResourceWithStreamingResponse,
    TrafficResource,
    TrafficResourceWithRawResponse,
    TrafficResourceWithStreamingResponse,
)
from .vulnerability_alerts import (
    AsyncVulnerabilityAlertsResource,
    AsyncVulnerabilityAlertsResourceWithRawResponse,
    AsyncVulnerabilityAlertsResourceWithStreamingResponse,
    VulnerabilityAlertsResource,
    VulnerabilityAlertsResourceWithRawResponse,
    VulnerabilityAlertsResourceWithStreamingResponse,
)

__all__ = ["ReposResource", "AsyncReposResource"]


class ReposResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def assignees(self) -> AssigneesResource:
        return AssigneesResource(self._client)

    @cached_property
    def attestations(self) -> AttestationsResource:
        return AttestationsResource(self._client)

    @cached_property
    def autolinks(self) -> AutolinksResource:
        return AutolinksResource(self._client)

    @cached_property
    def automated_security_fixes(self) -> AutomatedSecurityFixesResource:
        return AutomatedSecurityFixesResource(self._client)

    @cached_property
    def branches(self) -> BranchesResource:
        return BranchesResource(self._client)

    @cached_property
    def check_runs(self) -> CheckRunsResource:
        return CheckRunsResource(self._client)

    @cached_property
    def check_suites(self) -> CheckSuitesResource:
        return CheckSuitesResource(self._client)

    @cached_property
    def code_scanning(self) -> CodeScanningResource:
        return CodeScanningResource(self._client)

    @cached_property
    def codeowners(self) -> CodeownersResource:
        return CodeownersResource(self._client)

    @cached_property
    def codespaces(self) -> CodespacesResource:
        return CodespacesResource(self._client)

    @cached_property
    def collaborators(self) -> CollaboratorsResource:
        return CollaboratorsResource(self._client)

    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def commits(self) -> CommitsResource:
        return CommitsResource(self._client)

    @cached_property
    def community(self) -> CommunityResource:
        return CommunityResource(self._client)

    @cached_property
    def contents(self) -> ContentsResource:
        return ContentsResource(self._client)

    @cached_property
    def dependabot(self) -> DependabotResource:
        return DependabotResource(self._client)

    @cached_property
    def dependency_graph(self) -> DependencyGraphResource:
        return DependencyGraphResource(self._client)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        return DeploymentsResource(self._client)

    @cached_property
    def environments(self) -> EnvironmentsResource:
        return EnvironmentsResource(self._client)

    @cached_property
    def forks(self) -> ForksResource:
        return ForksResource(self._client)

    @cached_property
    def git(self) -> GitResource:
        return GitResource(self._client)

    @cached_property
    def hooks(self) -> HooksResource:
        return HooksResource(self._client)

    @cached_property
    def import_(self) -> ImportResource:
        return ImportResource(self._client)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResource:
        return InteractionLimitsResource(self._client)

    @cached_property
    def invitations(self) -> InvitationsResource:
        return InvitationsResource(self._client)

    @cached_property
    def issues(self) -> IssuesResource:
        return IssuesResource(self._client)

    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        return LabelsResource(self._client)

    @cached_property
    def milestones(self) -> MilestonesResource:
        return MilestonesResource(self._client)

    @cached_property
    def notifications(self) -> NotificationsResource:
        return NotificationsResource(self._client)

    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def private_vulnerability_reporting(self) -> PrivateVulnerabilityReportingResource:
        return PrivateVulnerabilityReportingResource(self._client)

    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def properties(self) -> PropertiesResource:
        return PropertiesResource(self._client)

    @cached_property
    def pulls(self) -> PullsResource:
        return PullsResource(self._client)

    @cached_property
    def readme(self) -> ReadmeResource:
        return ReadmeResource(self._client)

    @cached_property
    def releases(self) -> ReleasesResource:
        return ReleasesResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def rulesets(self) -> RulesetsResource:
        return RulesetsResource(self._client)

    @cached_property
    def secret_scanning(self) -> SecretScanningResource:
        return SecretScanningResource(self._client)

    @cached_property
    def security_advisories(self) -> SecurityAdvisoriesResource:
        return SecurityAdvisoriesResource(self._client)

    @cached_property
    def stats(self) -> StatsResource:
        return StatsResource(self._client)

    @cached_property
    def subscription(self) -> SubscriptionResource:
        return SubscriptionResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def topics(self) -> TopicsResource:
        return TopicsResource(self._client)

    @cached_property
    def traffic(self) -> TrafficResource:
        return TrafficResource(self._client)

    @cached_property
    def vulnerability_alerts(self) -> VulnerabilityAlertsResource:
        return VulnerabilityAlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ReposResourceWithStreamingResponse(self)

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
    ) -> FullRepository:
        """
        The `parent` and `source` objects are present when the repository is a fork.
        `parent` is the repository this repository was forked from, `source` is the
        ultimate source for the network.

        > [!NOTE] In order to see the `security_and_analysis` block for a repository you
        > must have admin permissions for the repository or be an owner or security
        > manager for the organization that owns the repository. For more information,
        > see
        > "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

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
            f"/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    def update(
        self,
        repo: str,
        *,
        owner: str,
        allow_auto_merge: bool | NotGiven = NOT_GIVEN,
        allow_forking: bool | NotGiven = NOT_GIVEN,
        allow_merge_commit: bool | NotGiven = NOT_GIVEN,
        allow_rebase_merge: bool | NotGiven = NOT_GIVEN,
        allow_squash_merge: bool | NotGiven = NOT_GIVEN,
        allow_update_branch: bool | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        default_branch: str | NotGiven = NOT_GIVEN,
        delete_branch_on_merge: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        has_issues: bool | NotGiven = NOT_GIVEN,
        has_projects: bool | NotGiven = NOT_GIVEN,
        has_wiki: bool | NotGiven = NOT_GIVEN,
        homepage: str | NotGiven = NOT_GIVEN,
        is_template: bool | NotGiven = NOT_GIVEN,
        merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | NotGiven = NOT_GIVEN,
        merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        security_and_analysis: repo_update_params.SecurityAndAnalysis | None | NotGiven = NOT_GIVEN,
        squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | NotGiven = NOT_GIVEN,
        squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | NotGiven = NOT_GIVEN,
        use_squash_pr_title_as_default: bool | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        web_commit_signoff_required: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """
        **Note**: To edit a repository's topics, use the
        [Replace all repository topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics)
        endpoint.

        Args:
          allow_auto_merge: Either `true` to allow auto-merge on pull requests, or `false` to disallow
              auto-merge.

          allow_forking: Either `true` to allow private forks, or `false` to prevent private forks.

          allow_merge_commit: Either `true` to allow merging pull requests with a merge commit, or `false` to
              prevent merging pull requests with merge commits.

          allow_rebase_merge: Either `true` to allow rebase-merging pull requests, or `false` to prevent
              rebase-merging.

          allow_squash_merge: Either `true` to allow squash-merging pull requests, or `false` to prevent
              squash-merging.

          allow_update_branch: Either `true` to always allow a pull request head branch that is behind its base
              branch to be updated even if it is not required to be up to date before merging,
              or false otherwise.

          archived: Whether to archive this repository. `false` will unarchive a previously archived
              repository.

          default_branch: Updates the default branch for this repository.

          delete_branch_on_merge: Either `true` to allow automatically deleting head branches when pull requests
              are merged, or `false` to prevent automatic deletion.

          description: A short description of the repository.

          has_issues: Either `true` to enable issues for this repository or `false` to disable them.

          has_projects: Either `true` to enable projects for this repository or `false` to disable them.
              **Note:** If you're creating a repository in an organization that has disabled
              repository projects, the default is `false`, and if you pass `true`, the API
              returns an error.

          has_wiki: Either `true` to enable the wiki for this repository or `false` to disable it.

          homepage: A URL with more information about the repository.

          is_template: Either `true` to make this repo available as a template repository or `false` to
              prevent it.

          merge_commit_message: The default value for a merge commit message.

              - `PR_TITLE` - default to the pull request's title.
              - `PR_BODY` - default to the pull request's body.
              - `BLANK` - default to a blank commit message.

          merge_commit_title: Required when using `merge_commit_message`.

              The default value for a merge commit title.

              - `PR_TITLE` - default to the pull request's title.
              - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g.,
                Merge pull request #123 from branch-name).

          name: The name of the repository.

          private: Either `true` to make the repository private or `false` to make it public.
              Default: `false`.
              **Note**: You will get a `422` error if the organization restricts
              [changing repository visibility](https://docs.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories)
              to organization owners and a non-owner tries to change the value of private.

          security_and_analysis: Specify which security and analysis features to enable or disable for the
              repository.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              For example, to enable GitHub Advanced Security, use this data in the body of
              the `PATCH` request:
              `{ "security_and_analysis": {"advanced_security": { "status": "enabled" } } }`.

              You can check which security and analysis features are currently enabled by
              using a `GET /repos/{owner}/{repo}` request.

          squash_merge_commit_message:
              The default value for a squash merge commit message:

              - `PR_BODY` - default to the pull request's body.
              - `COMMIT_MESSAGES` - default to the branch's commit messages.
              - `BLANK` - default to a blank commit message.

          squash_merge_commit_title: Required when using `squash_merge_commit_message`.

              The default value for a squash merge commit title:

              - `PR_TITLE` - default to the pull request's title.
              - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or
                the pull request's title (when more than one commit).

          use_squash_pr_title_as_default: Either `true` to allow squash-merge commits to use pull request title, or
              `false` to use commit message. \\**\\**This property is closing down. Please use
              `squash_merge_commit_title` instead.

          visibility: The visibility of the repository.

          web_commit_signoff_required: Either `true` to require contributors to sign off on web-based commits, or
              `false` to not require contributors to sign off on web-based commits.

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
            f"/repos/{owner}/{repo}",
            body=maybe_transform(
                {
                    "allow_auto_merge": allow_auto_merge,
                    "allow_forking": allow_forking,
                    "allow_merge_commit": allow_merge_commit,
                    "allow_rebase_merge": allow_rebase_merge,
                    "allow_squash_merge": allow_squash_merge,
                    "allow_update_branch": allow_update_branch,
                    "archived": archived,
                    "default_branch": default_branch,
                    "delete_branch_on_merge": delete_branch_on_merge,
                    "description": description,
                    "has_issues": has_issues,
                    "has_projects": has_projects,
                    "has_wiki": has_wiki,
                    "homepage": homepage,
                    "is_template": is_template,
                    "merge_commit_message": merge_commit_message,
                    "merge_commit_title": merge_commit_title,
                    "name": name,
                    "private": private,
                    "security_and_analysis": security_and_analysis,
                    "squash_merge_commit_message": squash_merge_commit_message,
                    "squash_merge_commit_title": squash_merge_commit_title,
                    "use_squash_pr_title_as_default": use_squash_pr_title_as_default,
                    "visibility": visibility,
                    "web_commit_signoff_required": web_commit_signoff_required,
                },
                repo_update_params.RepoUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    def delete(
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
        Deleting a repository requires admin access.

        If an organization owner has configured the organization to prevent members from
        deleting organization-owned repositories, you will get a `403 Forbidden`
        response.

        OAuth app tokens and personal access tokens (classic) need the `delete_repo`
        scope to use this endpoint.

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
            f"/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def compare_commits(
        self,
        basehead: str,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCompareCommitsResponse:
        """Compares two commits against one another.

        You can compare refs (branches or
        tags) and commit SHAs in the same repository, or you can compare refs and commit
        SHAs that exist in different repositories within the same repository network,
        including fork branches. For more information about how to view a repository's
        network, see
        "[Understanding connections between repositories](https://docs.github.com/repositories/viewing-activity-and-data-for-your-repository/understanding-connections-between-repositories)."

        This endpoint is equivalent to running the `git log BASE..HEAD` command, but it
        returns commits in a different order. The `git log BASE..HEAD` command returns
        commits in reverse chronological order, whereas the API returns commits in
        chronological order.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.diff`**: Returns the diff of the commit.
        - **`application/vnd.github.patch`**: Returns the patch of the commit. Diffs
          with binary data will have no `patch` property.

        The API response includes details about the files that were changed between the
        two commits. This includes the status of the change (if a file was added,
        removed, modified, or renamed), and details of the change itself. For example,
        files with a `renamed` status have a `previous_filename` field showing the
        previous filename of the file, and files with a `modified` status have a `patch`
        field showing the changes made to the file.

        When calling this endpoint without any paging parameter (`per_page` or `page`),
        the returned list is limited to 250 commits, and the last commit in the list is
        the most recent of the entire comparison.

        **Working with large comparisons**

        To process a response with a large number of commits, use a query parameter
        (`per_page` or `page`) to paginate the results. When using pagination:

        - The list of changed files is only shown on the first page of results, and it
          includes up to 300 changed files for the entire comparison.
        - The results are returned in chronological order, but the last commit in the
          returned list may not be the most recent one in the entire set if there are
          more pages of results.

        For more information on working with pagination, see
        "[Using pagination in the REST API](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api)."

        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The `verification` object includes the
        following fields:

        | Name          | Type      | Description                                                                                      |
        | ------------- | --------- | ------------------------------------------------------------------------------------------------ |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                  |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                |
        | `payload`     | `string`  | The value that was signed.                                                                       |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                   |

        These are the possible values for `reason` in the `verification` object:

        | Value                    | Description                                                                                                                     |
        | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
        | `expired_key`            | The key that made the signature is expired.                                                                                     |
        | `not_signing_key`        | The "signing" flag is not among the usage flags in the GPG key that made the signature.                                         |
        | `gpgverify_error`        | There was an error communicating with the signature verification service.                                                       |
        | `gpgverify_unavailable`  | The signature verification service is currently unavailable.                                                                    |
        | `unsigned`               | The object does not include a signature.                                                                                        |
        | `unknown_signature_type` | A non-PGP signature was found in the commit.                                                                                    |
        | `no_user`                | No user was associated with the `committer` email address in the commit.                                                        |
        | `unverified_email`       | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. |
        | `bad_email`              | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature.           |
        | `unknown_key`            | The key that made the signature has not been registered with any user's account.                                                |
        | `malformed_signature`    | There was an error parsing the signature.                                                                                       |
        | `invalid`                | The signature could not be cryptographically verified using the key whose key-id was found in the signature.                    |
        | `valid`                  | None of the above errors applied, so the signature is considered to be verified.                                                |

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not basehead:
            raise ValueError(f"Expected a non-empty value for `basehead` but received {basehead!r}")
        return self._get(
            f"/repos/{owner}/{repo}/compare/{basehead}",
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
                    repo_compare_commits_params.RepoCompareCommitsParams,
                ),
            ),
            cast_to=RepoCompareCommitsResponse,
        )

    def create_commit_status(
        self,
        sha: str,
        *,
        owner: str,
        repo: str,
        state: Literal["error", "failure", "pending", "success"],
        context: str | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        target_url: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Status:
        """
        Users with push access in a repository can create commit statuses for a given
        SHA.

        Note: there is a limit of 1000 statuses per `sha` and `context` within a
        repository. Attempts to create more than 1000 statuses will result in a
        validation error.

        Args:
          state: The state of the status.

          context: A string label to differentiate this status from the status of other systems.
              This field is case-insensitive.

          description: A short description of the status.

          target_url: The target URL to associate with this status. This URL will be linked from the
              GitHub UI to allow users to easily see the source of the status.
              For example, if your continuous integration system is posting build status, you
              would want to provide the deep link for the build output for this specific
              SHA:
              `http://ci.example.com/user/repo/build/sha`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not sha:
            raise ValueError(f"Expected a non-empty value for `sha` but received {sha!r}")
        return self._post(
            f"/repos/{owner}/{repo}/statuses/{sha}",
            body=maybe_transform(
                {
                    "state": state,
                    "context": context,
                    "description": description,
                    "target_url": target_url,
                },
                repo_create_commit_status_params.RepoCreateCommitStatusParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Status,
        )

    def create_dispatch_event(
        self,
        repo: str,
        *,
        owner: str,
        event_type: str,
        client_payload: dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can use this endpoint to trigger a webhook event called
        `repository_dispatch` when you want activity that happens outside of GitHub to
        trigger a GitHub Actions workflow or GitHub App webhook. You must configure your
        GitHub Actions workflow or GitHub App to run when the `repository_dispatch`
        event occurs. For an example `repository_dispatch` webhook payload, see
        "[RepositoryDispatchEvent](https://docs.github.com/webhooks/event-payloads/#repository_dispatch)."

        The `client_payload` parameter is available for any extra information that your
        workflow might need. This parameter is a JSON payload that will be passed on
        when the webhook event is dispatched. For example, the `client_payload` can
        include a message that a user would like to send using a GitHub Actions
        workflow. Or the `client_payload` can be used as a test to debug your workflow.

        This input example shows how you can use the `client_payload` as a test to debug
        your workflow.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          event_type: A custom webhook event name. Must be 100 characters or fewer.

          client_payload: JSON payload with extra information about the webhook event that your action or
              workflow may use. The maximum number of top-level properties is 10. The total
              size of the JSON payload must be less than 64KB.

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
        return self._post(
            f"/repos/{owner}/{repo}/dispatches",
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "client_payload": client_payload,
                },
                repo_create_dispatch_event_params.RepoCreateDispatchEventParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_from_template(
        self,
        template_repo: str,
        *,
        template_owner: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        include_all_branches: bool | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """Creates a new repository using a repository template.

        Use the `template_owner`
        and `template_repo` route parameters to specify the repository to use as the
        template. If the repository is not public, the authenticated user must own or be
        a member of an organization that owns the repository. To check if a repository
        is available to use as a template, get the repository's information using the
        [Get a repository](https://docs.github.com/rest/repos/repos#get-a-repository)
        endpoint and check that the `is_template` key is `true`.

        OAuth app tokens and personal access tokens (classic) need the `public_repo` or
        `repo` scope to create a public repository, and `repo` scope to create a private
        repository.

        Args:
          name: The name of the new repository.

          description: A short description of the new repository.

          include_all_branches: Set to `true` to include the directory structure and files from all branches in
              the template repository, and not just the default branch. Default: `false`.

          owner: The organization or person who will own the new repository. To create a new
              repository in an organization, the authenticated user must be a member of the
              specified organization.

          private: Either `true` to create a new private repository or `false` to create a new
              public one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_owner:
            raise ValueError(f"Expected a non-empty value for `template_owner` but received {template_owner!r}")
        if not template_repo:
            raise ValueError(f"Expected a non-empty value for `template_repo` but received {template_repo!r}")
        return self._post(
            f"/repos/{template_owner}/{template_repo}/generate",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "include_all_branches": include_all_branches,
                    "owner": owner,
                    "private": private,
                },
                repo_create_from_template_params.RepoCreateFromTemplateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    def download_tarball(
        self,
        ref: str,
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
        """Gets a redirect URL to download a tar archive for a repository.

        If you omit
        `:ref`, the repository’s default branch (usually `main`) will be used. Please
        make sure your HTTP framework is configured to follow redirects or you will need
        to use the `Location` header to make a second `GET` request.

        > [!NOTE] For private repositories, these links are temporary and expire after
        > five minutes.

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/repos/{owner}/{repo}/tarball/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def download_zipball(
        self,
        ref: str,
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
        """Gets a redirect URL to download a zip archive for a repository.

        If you omit
        `:ref`, the repository’s default branch (usually `main`) will be used. Please
        make sure your HTTP framework is configured to follow redirects or you will need
        to use the `Location` header to make a second `GET` request.

        > [!NOTE] For private repositories, these links are temporary and expire after
        > five minutes. If the repository is empty, you will receive a 404 when you
        > follow the redirect.

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/repos/{owner}/{repo}/zipball/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_code_security_configuration(
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
    ) -> RepoGetCodeSecurityConfigurationResponse:
        """
        Get the code security configuration that manages a repository's code security
        settings.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

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
            f"/repos/{owner}/{repo}/code-security-configuration",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepoGetCodeSecurityConfigurationResponse,
        )

    def get_installation(
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
    ) -> Installation:
        """
        Enables an authenticated GitHub App to find the repository's installation
        information. The installation's account type will be either an organization or a
        user account, depending which account the repository belongs to.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

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
            f"/repos/{owner}/{repo}/installation",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Installation,
        )

    def get_license(
        self,
        repo: str,
        *,
        owner: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoGetLicenseResponse:
        """
        This method returns the contents of the repository's license file, if one is
        detected.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw contents of the
          license.
        - **`application/vnd.github.html+json`**: Returns the license contents in HTML.
          Markup languages are rendered to HTML using GitHub's open-source
          [Markup library](https://github.com/github/markup).

        Args:
          ref: The Git reference for the results you want to list. The `ref` for a branch can
              be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To
              reference a pull request use `refs/pull/<number>/merge`.

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
            f"/repos/{owner}/{repo}/license",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ref": ref}, repo_get_license_params.RepoGetLicenseParams),
            ),
            cast_to=RepoGetLicenseResponse,
        )

    def list_activity(
        self,
        repo: str,
        *,
        owner: str,
        activity_type: Literal["push", "force_push", "branch_creation", "branch_deletion", "pr_merge", "merge_queue_merge"] | NotGiven = NOT_GIVEN,
        actor: str | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        time_period: Literal["day", "week", "month", "quarter", "year"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListActivityResponse:
        """
        Lists a detailed history of changes to a repository, such as pushes, merges,
        force pushes, and branch changes, and associates these changes with commits and
        users.

        For more information about viewing repository activity, see
        "[Viewing activity and data for your repository](https://docs.github.com/repositories/viewing-activity-and-data-for-your-repository)."

        Args:
          activity_type: The activity type to filter by.

              For example, you can choose to filter by "force_push", to see all force pushes
              to the repository.

          actor: The GitHub username to use to filter by the actor who performed the activity.

          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          direction: The direction to sort the results by.

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          ref: The Git reference for the activities you want to list.

              The `ref` for a branch can be formatted either as `refs/heads/BRANCH_NAME` or
              `BRANCH_NAME`, where `BRANCH_NAME` is the name of your branch.

          time_period: The time period to filter by.

              For example, `day` will filter for activity that occurred in the past 24 hours,
              and `week` will filter for activity that occurred in the past 7 days (168
              hours).

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
            f"/repos/{owner}/{repo}/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "activity_type": activity_type,
                        "actor": actor,
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "per_page": per_page,
                        "ref": ref,
                        "time_period": time_period,
                    },
                    repo_list_activity_params.RepoListActivityParams,
                ),
            ),
            cast_to=RepoListActivityResponse,
        )

    def list_contributors(
        self,
        repo: str,
        *,
        owner: str,
        anon: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListContributorsResponse:
        """
        Lists contributors to the specified repository and sorts them by the number of
        commits per contributor in descending order. This endpoint may return
        information that is a few hours old because the GitHub REST API caches
        contributor data to improve performance.

        GitHub identifies contributors by author email address. This endpoint groups
        contribution counts by GitHub user, which includes all associated email
        addresses. To improve performance, only the first 500 author email addresses in
        the repository link to GitHub users. The rest will appear as anonymous
        contributors without associated GitHub user information.

        Args:
          anon: Set to `1` or `true` to include anonymous contributors in results.

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
            f"/repos/{owner}/{repo}/contributors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "anon": anon,
                        "page": page,
                        "per_page": per_page,
                    },
                    repo_list_contributors_params.RepoListContributorsParams,
                ),
            ),
            cast_to=RepoListContributorsResponse,
        )

    def list_events(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListEventsResponse:
        """> [!NOTE] This API is not built to serve real-time use cases.

        Depending on the
        > time of day, event latency can be anywhere from 30s to 6h.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/events",
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
                    repo_list_events_params.RepoListEventsParams,
                ),
            ),
            cast_to=RepoListEventsResponse,
        )

    def list_languages(
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
    ) -> RepoListLanguagesResponse:
        """Lists languages for the specified repository.

        The value shown for each language
        is the number of bytes of code written in that language.

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
            f"/repos/{owner}/{repo}/languages",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepoListLanguagesResponse,
        )

    def list_stargazers(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListStargazersResponse:
        """
        Lists the people that have starred the repository.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.star+json`**: Includes a timestamp of when the star
          was created.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return cast(
            RepoListStargazersResponse,
            self._get(
                f"/repos/{owner}/{repo}/stargazers",
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
                        repo_list_stargazers_params.RepoListStargazersParams,
                    ),
                ),
                cast_to=cast(Any, RepoListStargazersResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list_teams(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListTeamsResponse:
        """
        Lists the teams that have access to the specified repository and that are also
        visible to the authenticated user.

        For a public repository, a team is listed only if that team added the public
        repository explicitly.

        OAuth app tokens and personal access tokens (classic) need the `public_repo` or
        `repo` scope to use this endpoint with a public repository, and `repo` scope to
        use this endpoint with a private repository.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/teams",
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
                    repo_list_teams_params.RepoListTeamsParams,
                ),
            ),
            cast_to=RepoListTeamsResponse,
        )

    def list_watchers(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListWatchersResponse:
        """
        Lists the people watching the specified repository.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/subscribers",
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
                    repo_list_watchers_params.RepoListWatchersParams,
                ),
            ),
            cast_to=RepoListWatchersResponse,
        )

    def merge_branch(
        self,
        repo: str,
        *,
        owner: str,
        base: str,
        head: str,
        commit_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Commit:
        """
        Merge a branch

        Args:
          base: The name of the base branch that the head will be merged into.

          head: The head to merge. This can be a branch name or a commit SHA1.

          commit_message: Commit message to use for the merge commit. If omitted, a default message will
              be used.

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
            f"/repos/{owner}/{repo}/merges",
            body=maybe_transform(
                {
                    "base": base,
                    "head": head,
                    "commit_message": commit_message,
                },
                repo_merge_branch_params.RepoMergeBranchParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Commit,
        )

    def sync_with_upstream(
        self,
        repo: str,
        *,
        owner: str,
        branch: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoSyncWithUpstreamResponse:
        """
        Sync a branch of a forked repository to keep it up-to-date with the upstream
        repository.

        Args:
          branch: The name of the branch which should be updated to match upstream.

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
            f"/repos/{owner}/{repo}/merge-upstream",
            body=maybe_transform({"branch": branch}, repo_sync_with_upstream_params.RepoSyncWithUpstreamParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepoSyncWithUpstreamResponse,
        )

    def transfer(
        self,
        repo: str,
        *,
        owner: str,
        new_owner: str,
        new_name: str | NotGiven = NOT_GIVEN,
        team_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MinimalRepository:
        """
        A transfer request will need to be accepted by the new owner when transferring a
        personal repository to another user. The response will contain the original
        `owner`, and the transfer will continue asynchronously. For more details on the
        requirements to transfer personal and organization-owned repositories, see
        [about repository transfers](https://docs.github.com/articles/about-repository-transfers/).

        Args:
          new_owner: The username or organization name the repository will be transferred to.

          new_name: The new name to be given to the repository.

          team_ids: ID of the team or teams to add to the repository. Teams can only be added to
              organization-owned repositories.

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
            f"/repos/{owner}/{repo}/transfer",
            body=maybe_transform(
                {
                    "new_owner": new_owner,
                    "new_name": new_name,
                    "team_ids": team_ids,
                },
                repo_transfer_params.RepoTransferParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MinimalRepository,
        )


class AsyncReposResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def assignees(self) -> AsyncAssigneesResource:
        return AsyncAssigneesResource(self._client)

    @cached_property
    def attestations(self) -> AsyncAttestationsResource:
        return AsyncAttestationsResource(self._client)

    @cached_property
    def autolinks(self) -> AsyncAutolinksResource:
        return AsyncAutolinksResource(self._client)

    @cached_property
    def automated_security_fixes(self) -> AsyncAutomatedSecurityFixesResource:
        return AsyncAutomatedSecurityFixesResource(self._client)

    @cached_property
    def branches(self) -> AsyncBranchesResource:
        return AsyncBranchesResource(self._client)

    @cached_property
    def check_runs(self) -> AsyncCheckRunsResource:
        return AsyncCheckRunsResource(self._client)

    @cached_property
    def check_suites(self) -> AsyncCheckSuitesResource:
        return AsyncCheckSuitesResource(self._client)

    @cached_property
    def code_scanning(self) -> AsyncCodeScanningResource:
        return AsyncCodeScanningResource(self._client)

    @cached_property
    def codeowners(self) -> AsyncCodeownersResource:
        return AsyncCodeownersResource(self._client)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResource:
        return AsyncCodespacesResource(self._client)

    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResource:
        return AsyncCollaboratorsResource(self._client)

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def commits(self) -> AsyncCommitsResource:
        return AsyncCommitsResource(self._client)

    @cached_property
    def community(self) -> AsyncCommunityResource:
        return AsyncCommunityResource(self._client)

    @cached_property
    def contents(self) -> AsyncContentsResource:
        return AsyncContentsResource(self._client)

    @cached_property
    def dependabot(self) -> AsyncDependabotResource:
        return AsyncDependabotResource(self._client)

    @cached_property
    def dependency_graph(self) -> AsyncDependencyGraphResource:
        return AsyncDependencyGraphResource(self._client)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        return AsyncDeploymentsResource(self._client)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResource:
        return AsyncEnvironmentsResource(self._client)

    @cached_property
    def forks(self) -> AsyncForksResource:
        return AsyncForksResource(self._client)

    @cached_property
    def git(self) -> AsyncGitResource:
        return AsyncGitResource(self._client)

    @cached_property
    def hooks(self) -> AsyncHooksResource:
        return AsyncHooksResource(self._client)

    @cached_property
    def import_(self) -> AsyncImportResource:
        return AsyncImportResource(self._client)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResource:
        return AsyncInteractionLimitsResource(self._client)

    @cached_property
    def invitations(self) -> AsyncInvitationsResource:
        return AsyncInvitationsResource(self._client)

    @cached_property
    def issues(self) -> AsyncIssuesResource:
        return AsyncIssuesResource(self._client)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        return AsyncLabelsResource(self._client)

    @cached_property
    def milestones(self) -> AsyncMilestonesResource:
        return AsyncMilestonesResource(self._client)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        return AsyncNotificationsResource(self._client)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def private_vulnerability_reporting(self) -> AsyncPrivateVulnerabilityReportingResource:
        return AsyncPrivateVulnerabilityReportingResource(self._client)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        return AsyncPropertiesResource(self._client)

    @cached_property
    def pulls(self) -> AsyncPullsResource:
        return AsyncPullsResource(self._client)

    @cached_property
    def readme(self) -> AsyncReadmeResource:
        return AsyncReadmeResource(self._client)

    @cached_property
    def releases(self) -> AsyncReleasesResource:
        return AsyncReleasesResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def rulesets(self) -> AsyncRulesetsResource:
        return AsyncRulesetsResource(self._client)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResource:
        return AsyncSecretScanningResource(self._client)

    @cached_property
    def security_advisories(self) -> AsyncSecurityAdvisoriesResource:
        return AsyncSecurityAdvisoriesResource(self._client)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        return AsyncStatsResource(self._client)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResource:
        return AsyncSubscriptionResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def topics(self) -> AsyncTopicsResource:
        return AsyncTopicsResource(self._client)

    @cached_property
    def traffic(self) -> AsyncTrafficResource:
        return AsyncTrafficResource(self._client)

    @cached_property
    def vulnerability_alerts(self) -> AsyncVulnerabilityAlertsResource:
        return AsyncVulnerabilityAlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncReposResourceWithStreamingResponse(self)

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
    ) -> FullRepository:
        """
        The `parent` and `source` objects are present when the repository is a fork.
        `parent` is the repository this repository was forked from, `source` is the
        ultimate source for the network.

        > [!NOTE] In order to see the `security_and_analysis` block for a repository you
        > must have admin permissions for the repository or be an owner or security
        > manager for the organization that owns the repository. For more information,
        > see
        > "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

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
            f"/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    async def update(
        self,
        repo: str,
        *,
        owner: str,
        allow_auto_merge: bool | NotGiven = NOT_GIVEN,
        allow_forking: bool | NotGiven = NOT_GIVEN,
        allow_merge_commit: bool | NotGiven = NOT_GIVEN,
        allow_rebase_merge: bool | NotGiven = NOT_GIVEN,
        allow_squash_merge: bool | NotGiven = NOT_GIVEN,
        allow_update_branch: bool | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        default_branch: str | NotGiven = NOT_GIVEN,
        delete_branch_on_merge: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        has_issues: bool | NotGiven = NOT_GIVEN,
        has_projects: bool | NotGiven = NOT_GIVEN,
        has_wiki: bool | NotGiven = NOT_GIVEN,
        homepage: str | NotGiven = NOT_GIVEN,
        is_template: bool | NotGiven = NOT_GIVEN,
        merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | NotGiven = NOT_GIVEN,
        merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        security_and_analysis: repo_update_params.SecurityAndAnalysis | None | NotGiven = NOT_GIVEN,
        squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | NotGiven = NOT_GIVEN,
        squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | NotGiven = NOT_GIVEN,
        use_squash_pr_title_as_default: bool | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        web_commit_signoff_required: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """
        **Note**: To edit a repository's topics, use the
        [Replace all repository topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics)
        endpoint.

        Args:
          allow_auto_merge: Either `true` to allow auto-merge on pull requests, or `false` to disallow
              auto-merge.

          allow_forking: Either `true` to allow private forks, or `false` to prevent private forks.

          allow_merge_commit: Either `true` to allow merging pull requests with a merge commit, or `false` to
              prevent merging pull requests with merge commits.

          allow_rebase_merge: Either `true` to allow rebase-merging pull requests, or `false` to prevent
              rebase-merging.

          allow_squash_merge: Either `true` to allow squash-merging pull requests, or `false` to prevent
              squash-merging.

          allow_update_branch: Either `true` to always allow a pull request head branch that is behind its base
              branch to be updated even if it is not required to be up to date before merging,
              or false otherwise.

          archived: Whether to archive this repository. `false` will unarchive a previously archived
              repository.

          default_branch: Updates the default branch for this repository.

          delete_branch_on_merge: Either `true` to allow automatically deleting head branches when pull requests
              are merged, or `false` to prevent automatic deletion.

          description: A short description of the repository.

          has_issues: Either `true` to enable issues for this repository or `false` to disable them.

          has_projects: Either `true` to enable projects for this repository or `false` to disable them.
              **Note:** If you're creating a repository in an organization that has disabled
              repository projects, the default is `false`, and if you pass `true`, the API
              returns an error.

          has_wiki: Either `true` to enable the wiki for this repository or `false` to disable it.

          homepage: A URL with more information about the repository.

          is_template: Either `true` to make this repo available as a template repository or `false` to
              prevent it.

          merge_commit_message: The default value for a merge commit message.

              - `PR_TITLE` - default to the pull request's title.
              - `PR_BODY` - default to the pull request's body.
              - `BLANK` - default to a blank commit message.

          merge_commit_title: Required when using `merge_commit_message`.

              The default value for a merge commit title.

              - `PR_TITLE` - default to the pull request's title.
              - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g.,
                Merge pull request #123 from branch-name).

          name: The name of the repository.

          private: Either `true` to make the repository private or `false` to make it public.
              Default: `false`.
              **Note**: You will get a `422` error if the organization restricts
              [changing repository visibility](https://docs.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories)
              to organization owners and a non-owner tries to change the value of private.

          security_and_analysis: Specify which security and analysis features to enable or disable for the
              repository.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              For example, to enable GitHub Advanced Security, use this data in the body of
              the `PATCH` request:
              `{ "security_and_analysis": {"advanced_security": { "status": "enabled" } } }`.

              You can check which security and analysis features are currently enabled by
              using a `GET /repos/{owner}/{repo}` request.

          squash_merge_commit_message:
              The default value for a squash merge commit message:

              - `PR_BODY` - default to the pull request's body.
              - `COMMIT_MESSAGES` - default to the branch's commit messages.
              - `BLANK` - default to a blank commit message.

          squash_merge_commit_title: Required when using `squash_merge_commit_message`.

              The default value for a squash merge commit title:

              - `PR_TITLE` - default to the pull request's title.
              - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or
                the pull request's title (when more than one commit).

          use_squash_pr_title_as_default: Either `true` to allow squash-merge commits to use pull request title, or
              `false` to use commit message. \\**\\**This property is closing down. Please use
              `squash_merge_commit_title` instead.

          visibility: The visibility of the repository.

          web_commit_signoff_required: Either `true` to require contributors to sign off on web-based commits, or
              `false` to not require contributors to sign off on web-based commits.

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
            f"/repos/{owner}/{repo}",
            body=await async_maybe_transform(
                {
                    "allow_auto_merge": allow_auto_merge,
                    "allow_forking": allow_forking,
                    "allow_merge_commit": allow_merge_commit,
                    "allow_rebase_merge": allow_rebase_merge,
                    "allow_squash_merge": allow_squash_merge,
                    "allow_update_branch": allow_update_branch,
                    "archived": archived,
                    "default_branch": default_branch,
                    "delete_branch_on_merge": delete_branch_on_merge,
                    "description": description,
                    "has_issues": has_issues,
                    "has_projects": has_projects,
                    "has_wiki": has_wiki,
                    "homepage": homepage,
                    "is_template": is_template,
                    "merge_commit_message": merge_commit_message,
                    "merge_commit_title": merge_commit_title,
                    "name": name,
                    "private": private,
                    "security_and_analysis": security_and_analysis,
                    "squash_merge_commit_message": squash_merge_commit_message,
                    "squash_merge_commit_title": squash_merge_commit_title,
                    "use_squash_pr_title_as_default": use_squash_pr_title_as_default,
                    "visibility": visibility,
                    "web_commit_signoff_required": web_commit_signoff_required,
                },
                repo_update_params.RepoUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    async def delete(
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
        Deleting a repository requires admin access.

        If an organization owner has configured the organization to prevent members from
        deleting organization-owned repositories, you will get a `403 Forbidden`
        response.

        OAuth app tokens and personal access tokens (classic) need the `delete_repo`
        scope to use this endpoint.

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
            f"/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def compare_commits(
        self,
        basehead: str,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoCompareCommitsResponse:
        """Compares two commits against one another.

        You can compare refs (branches or
        tags) and commit SHAs in the same repository, or you can compare refs and commit
        SHAs that exist in different repositories within the same repository network,
        including fork branches. For more information about how to view a repository's
        network, see
        "[Understanding connections between repositories](https://docs.github.com/repositories/viewing-activity-and-data-for-your-repository/understanding-connections-between-repositories)."

        This endpoint is equivalent to running the `git log BASE..HEAD` command, but it
        returns commits in a different order. The `git log BASE..HEAD` command returns
        commits in reverse chronological order, whereas the API returns commits in
        chronological order.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.diff`**: Returns the diff of the commit.
        - **`application/vnd.github.patch`**: Returns the patch of the commit. Diffs
          with binary data will have no `patch` property.

        The API response includes details about the files that were changed between the
        two commits. This includes the status of the change (if a file was added,
        removed, modified, or renamed), and details of the change itself. For example,
        files with a `renamed` status have a `previous_filename` field showing the
        previous filename of the file, and files with a `modified` status have a `patch`
        field showing the changes made to the file.

        When calling this endpoint without any paging parameter (`per_page` or `page`),
        the returned list is limited to 250 commits, and the last commit in the list is
        the most recent of the entire comparison.

        **Working with large comparisons**

        To process a response with a large number of commits, use a query parameter
        (`per_page` or `page`) to paginate the results. When using pagination:

        - The list of changed files is only shown on the first page of results, and it
          includes up to 300 changed files for the entire comparison.
        - The results are returned in chronological order, but the last commit in the
          returned list may not be the most recent one in the entire set if there are
          more pages of results.

        For more information on working with pagination, see
        "[Using pagination in the REST API](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api)."

        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The `verification` object includes the
        following fields:

        | Name          | Type      | Description                                                                                      |
        | ------------- | --------- | ------------------------------------------------------------------------------------------------ |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                  |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                |
        | `payload`     | `string`  | The value that was signed.                                                                       |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                   |

        These are the possible values for `reason` in the `verification` object:

        | Value                    | Description                                                                                                                     |
        | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
        | `expired_key`            | The key that made the signature is expired.                                                                                     |
        | `not_signing_key`        | The "signing" flag is not among the usage flags in the GPG key that made the signature.                                         |
        | `gpgverify_error`        | There was an error communicating with the signature verification service.                                                       |
        | `gpgverify_unavailable`  | The signature verification service is currently unavailable.                                                                    |
        | `unsigned`               | The object does not include a signature.                                                                                        |
        | `unknown_signature_type` | A non-PGP signature was found in the commit.                                                                                    |
        | `no_user`                | No user was associated with the `committer` email address in the commit.                                                        |
        | `unverified_email`       | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. |
        | `bad_email`              | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature.           |
        | `unknown_key`            | The key that made the signature has not been registered with any user's account.                                                |
        | `malformed_signature`    | There was an error parsing the signature.                                                                                       |
        | `invalid`                | The signature could not be cryptographically verified using the key whose key-id was found in the signature.                    |
        | `valid`                  | None of the above errors applied, so the signature is considered to be verified.                                                |

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not basehead:
            raise ValueError(f"Expected a non-empty value for `basehead` but received {basehead!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/compare/{basehead}",
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
                    repo_compare_commits_params.RepoCompareCommitsParams,
                ),
            ),
            cast_to=RepoCompareCommitsResponse,
        )

    async def create_commit_status(
        self,
        sha: str,
        *,
        owner: str,
        repo: str,
        state: Literal["error", "failure", "pending", "success"],
        context: str | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        target_url: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Status:
        """
        Users with push access in a repository can create commit statuses for a given
        SHA.

        Note: there is a limit of 1000 statuses per `sha` and `context` within a
        repository. Attempts to create more than 1000 statuses will result in a
        validation error.

        Args:
          state: The state of the status.

          context: A string label to differentiate this status from the status of other systems.
              This field is case-insensitive.

          description: A short description of the status.

          target_url: The target URL to associate with this status. This URL will be linked from the
              GitHub UI to allow users to easily see the source of the status.
              For example, if your continuous integration system is posting build status, you
              would want to provide the deep link for the build output for this specific
              SHA:
              `http://ci.example.com/user/repo/build/sha`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not sha:
            raise ValueError(f"Expected a non-empty value for `sha` but received {sha!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/statuses/{sha}",
            body=await async_maybe_transform(
                {
                    "state": state,
                    "context": context,
                    "description": description,
                    "target_url": target_url,
                },
                repo_create_commit_status_params.RepoCreateCommitStatusParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Status,
        )

    async def create_dispatch_event(
        self,
        repo: str,
        *,
        owner: str,
        event_type: str,
        client_payload: dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can use this endpoint to trigger a webhook event called
        `repository_dispatch` when you want activity that happens outside of GitHub to
        trigger a GitHub Actions workflow or GitHub App webhook. You must configure your
        GitHub Actions workflow or GitHub App to run when the `repository_dispatch`
        event occurs. For an example `repository_dispatch` webhook payload, see
        "[RepositoryDispatchEvent](https://docs.github.com/webhooks/event-payloads/#repository_dispatch)."

        The `client_payload` parameter is available for any extra information that your
        workflow might need. This parameter is a JSON payload that will be passed on
        when the webhook event is dispatched. For example, the `client_payload` can
        include a message that a user would like to send using a GitHub Actions
        workflow. Or the `client_payload` can be used as a test to debug your workflow.

        This input example shows how you can use the `client_payload` as a test to debug
        your workflow.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          event_type: A custom webhook event name. Must be 100 characters or fewer.

          client_payload: JSON payload with extra information about the webhook event that your action or
              workflow may use. The maximum number of top-level properties is 10. The total
              size of the JSON payload must be less than 64KB.

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
        return await self._post(
            f"/repos/{owner}/{repo}/dispatches",
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "client_payload": client_payload,
                },
                repo_create_dispatch_event_params.RepoCreateDispatchEventParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_from_template(
        self,
        template_repo: str,
        *,
        template_owner: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        include_all_branches: bool | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """Creates a new repository using a repository template.

        Use the `template_owner`
        and `template_repo` route parameters to specify the repository to use as the
        template. If the repository is not public, the authenticated user must own or be
        a member of an organization that owns the repository. To check if a repository
        is available to use as a template, get the repository's information using the
        [Get a repository](https://docs.github.com/rest/repos/repos#get-a-repository)
        endpoint and check that the `is_template` key is `true`.

        OAuth app tokens and personal access tokens (classic) need the `public_repo` or
        `repo` scope to create a public repository, and `repo` scope to create a private
        repository.

        Args:
          name: The name of the new repository.

          description: A short description of the new repository.

          include_all_branches: Set to `true` to include the directory structure and files from all branches in
              the template repository, and not just the default branch. Default: `false`.

          owner: The organization or person who will own the new repository. To create a new
              repository in an organization, the authenticated user must be a member of the
              specified organization.

          private: Either `true` to create a new private repository or `false` to create a new
              public one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_owner:
            raise ValueError(f"Expected a non-empty value for `template_owner` but received {template_owner!r}")
        if not template_repo:
            raise ValueError(f"Expected a non-empty value for `template_repo` but received {template_repo!r}")
        return await self._post(
            f"/repos/{template_owner}/{template_repo}/generate",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "include_all_branches": include_all_branches,
                    "owner": owner,
                    "private": private,
                },
                repo_create_from_template_params.RepoCreateFromTemplateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    async def download_tarball(
        self,
        ref: str,
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
        """Gets a redirect URL to download a tar archive for a repository.

        If you omit
        `:ref`, the repository’s default branch (usually `main`) will be used. Please
        make sure your HTTP framework is configured to follow redirects or you will need
        to use the `Location` header to make a second `GET` request.

        > [!NOTE] For private repositories, these links are temporary and expire after
        > five minutes.

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/repos/{owner}/{repo}/tarball/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def download_zipball(
        self,
        ref: str,
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
        """Gets a redirect URL to download a zip archive for a repository.

        If you omit
        `:ref`, the repository’s default branch (usually `main`) will be used. Please
        make sure your HTTP framework is configured to follow redirects or you will need
        to use the `Location` header to make a second `GET` request.

        > [!NOTE] For private repositories, these links are temporary and expire after
        > five minutes. If the repository is empty, you will receive a 404 when you
        > follow the redirect.

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/repos/{owner}/{repo}/zipball/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_code_security_configuration(
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
    ) -> RepoGetCodeSecurityConfigurationResponse:
        """
        Get the code security configuration that manages a repository's code security
        settings.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

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
            f"/repos/{owner}/{repo}/code-security-configuration",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepoGetCodeSecurityConfigurationResponse,
        )

    async def get_installation(
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
    ) -> Installation:
        """
        Enables an authenticated GitHub App to find the repository's installation
        information. The installation's account type will be either an organization or a
        user account, depending which account the repository belongs to.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

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
            f"/repos/{owner}/{repo}/installation",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Installation,
        )

    async def get_license(
        self,
        repo: str,
        *,
        owner: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoGetLicenseResponse:
        """
        This method returns the contents of the repository's license file, if one is
        detected.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw contents of the
          license.
        - **`application/vnd.github.html+json`**: Returns the license contents in HTML.
          Markup languages are rendered to HTML using GitHub's open-source
          [Markup library](https://github.com/github/markup).

        Args:
          ref: The Git reference for the results you want to list. The `ref` for a branch can
              be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To
              reference a pull request use `refs/pull/<number>/merge`.

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
            f"/repos/{owner}/{repo}/license",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ref": ref}, repo_get_license_params.RepoGetLicenseParams),
            ),
            cast_to=RepoGetLicenseResponse,
        )

    async def list_activity(
        self,
        repo: str,
        *,
        owner: str,
        activity_type: Literal["push", "force_push", "branch_creation", "branch_deletion", "pr_merge", "merge_queue_merge"] | NotGiven = NOT_GIVEN,
        actor: str | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        time_period: Literal["day", "week", "month", "quarter", "year"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListActivityResponse:
        """
        Lists a detailed history of changes to a repository, such as pushes, merges,
        force pushes, and branch changes, and associates these changes with commits and
        users.

        For more information about viewing repository activity, see
        "[Viewing activity and data for your repository](https://docs.github.com/repositories/viewing-activity-and-data-for-your-repository)."

        Args:
          activity_type: The activity type to filter by.

              For example, you can choose to filter by "force_push", to see all force pushes
              to the repository.

          actor: The GitHub username to use to filter by the actor who performed the activity.

          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          direction: The direction to sort the results by.

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          ref: The Git reference for the activities you want to list.

              The `ref` for a branch can be formatted either as `refs/heads/BRANCH_NAME` or
              `BRANCH_NAME`, where `BRANCH_NAME` is the name of your branch.

          time_period: The time period to filter by.

              For example, `day` will filter for activity that occurred in the past 24 hours,
              and `week` will filter for activity that occurred in the past 7 days (168
              hours).

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
            f"/repos/{owner}/{repo}/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "activity_type": activity_type,
                        "actor": actor,
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "per_page": per_page,
                        "ref": ref,
                        "time_period": time_period,
                    },
                    repo_list_activity_params.RepoListActivityParams,
                ),
            ),
            cast_to=RepoListActivityResponse,
        )

    async def list_contributors(
        self,
        repo: str,
        *,
        owner: str,
        anon: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListContributorsResponse:
        """
        Lists contributors to the specified repository and sorts them by the number of
        commits per contributor in descending order. This endpoint may return
        information that is a few hours old because the GitHub REST API caches
        contributor data to improve performance.

        GitHub identifies contributors by author email address. This endpoint groups
        contribution counts by GitHub user, which includes all associated email
        addresses. To improve performance, only the first 500 author email addresses in
        the repository link to GitHub users. The rest will appear as anonymous
        contributors without associated GitHub user information.

        Args:
          anon: Set to `1` or `true` to include anonymous contributors in results.

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
            f"/repos/{owner}/{repo}/contributors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "anon": anon,
                        "page": page,
                        "per_page": per_page,
                    },
                    repo_list_contributors_params.RepoListContributorsParams,
                ),
            ),
            cast_to=RepoListContributorsResponse,
        )

    async def list_events(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListEventsResponse:
        """> [!NOTE] This API is not built to serve real-time use cases.

        Depending on the
        > time of day, event latency can be anywhere from 30s to 6h.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/events",
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
                    repo_list_events_params.RepoListEventsParams,
                ),
            ),
            cast_to=RepoListEventsResponse,
        )

    async def list_languages(
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
    ) -> RepoListLanguagesResponse:
        """Lists languages for the specified repository.

        The value shown for each language
        is the number of bytes of code written in that language.

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
            f"/repos/{owner}/{repo}/languages",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepoListLanguagesResponse,
        )

    async def list_stargazers(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListStargazersResponse:
        """
        Lists the people that have starred the repository.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.star+json`**: Includes a timestamp of when the star
          was created.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return cast(
            RepoListStargazersResponse,
            await self._get(
                f"/repos/{owner}/{repo}/stargazers",
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
                        repo_list_stargazers_params.RepoListStargazersParams,
                    ),
                ),
                cast_to=cast(Any, RepoListStargazersResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list_teams(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListTeamsResponse:
        """
        Lists the teams that have access to the specified repository and that are also
        visible to the authenticated user.

        For a public repository, a team is listed only if that team added the public
        repository explicitly.

        OAuth app tokens and personal access tokens (classic) need the `public_repo` or
        `repo` scope to use this endpoint with a public repository, and `repo` scope to
        use this endpoint with a private repository.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/teams",
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
                    repo_list_teams_params.RepoListTeamsParams,
                ),
            ),
            cast_to=RepoListTeamsResponse,
        )

    async def list_watchers(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListWatchersResponse:
        """
        Lists the people watching the specified repository.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/subscribers",
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
                    repo_list_watchers_params.RepoListWatchersParams,
                ),
            ),
            cast_to=RepoListWatchersResponse,
        )

    async def merge_branch(
        self,
        repo: str,
        *,
        owner: str,
        base: str,
        head: str,
        commit_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Commit:
        """
        Merge a branch

        Args:
          base: The name of the base branch that the head will be merged into.

          head: The head to merge. This can be a branch name or a commit SHA1.

          commit_message: Commit message to use for the merge commit. If omitted, a default message will
              be used.

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
            f"/repos/{owner}/{repo}/merges",
            body=await async_maybe_transform(
                {
                    "base": base,
                    "head": head,
                    "commit_message": commit_message,
                },
                repo_merge_branch_params.RepoMergeBranchParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Commit,
        )

    async def sync_with_upstream(
        self,
        repo: str,
        *,
        owner: str,
        branch: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoSyncWithUpstreamResponse:
        """
        Sync a branch of a forked repository to keep it up-to-date with the upstream
        repository.

        Args:
          branch: The name of the branch which should be updated to match upstream.

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
            f"/repos/{owner}/{repo}/merge-upstream",
            body=await async_maybe_transform({"branch": branch}, repo_sync_with_upstream_params.RepoSyncWithUpstreamParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepoSyncWithUpstreamResponse,
        )

    async def transfer(
        self,
        repo: str,
        *,
        owner: str,
        new_owner: str,
        new_name: str | NotGiven = NOT_GIVEN,
        team_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MinimalRepository:
        """
        A transfer request will need to be accepted by the new owner when transferring a
        personal repository to another user. The response will contain the original
        `owner`, and the transfer will continue asynchronously. For more details on the
        requirements to transfer personal and organization-owned repositories, see
        [about repository transfers](https://docs.github.com/articles/about-repository-transfers/).

        Args:
          new_owner: The username or organization name the repository will be transferred to.

          new_name: The new name to be given to the repository.

          team_ids: ID of the team or teams to add to the repository. Teams can only be added to
              organization-owned repositories.

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
            f"/repos/{owner}/{repo}/transfer",
            body=await async_maybe_transform(
                {
                    "new_owner": new_owner,
                    "new_name": new_name,
                    "team_ids": team_ids,
                },
                repo_transfer_params.RepoTransferParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MinimalRepository,
        )


class ReposResourceWithRawResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.retrieve = to_raw_response_wrapper(
            repos.retrieve,
        )
        self.update = to_raw_response_wrapper(
            repos.update,
        )
        self.delete = to_raw_response_wrapper(
            repos.delete,
        )
        self.compare_commits = to_raw_response_wrapper(
            repos.compare_commits,
        )
        self.create_commit_status = to_raw_response_wrapper(
            repos.create_commit_status,
        )
        self.create_dispatch_event = to_raw_response_wrapper(
            repos.create_dispatch_event,
        )
        self.create_from_template = to_raw_response_wrapper(
            repos.create_from_template,
        )
        self.download_tarball = to_raw_response_wrapper(
            repos.download_tarball,
        )
        self.download_zipball = to_raw_response_wrapper(
            repos.download_zipball,
        )
        self.get_code_security_configuration = to_raw_response_wrapper(
            repos.get_code_security_configuration,
        )
        self.get_installation = to_raw_response_wrapper(
            repos.get_installation,
        )
        self.get_license = to_raw_response_wrapper(
            repos.get_license,
        )
        self.list_activity = to_raw_response_wrapper(
            repos.list_activity,
        )
        self.list_contributors = to_raw_response_wrapper(
            repos.list_contributors,
        )
        self.list_events = to_raw_response_wrapper(
            repos.list_events,
        )
        self.list_languages = to_raw_response_wrapper(
            repos.list_languages,
        )
        self.list_stargazers = to_raw_response_wrapper(
            repos.list_stargazers,
        )
        self.list_teams = to_raw_response_wrapper(
            repos.list_teams,
        )
        self.list_watchers = to_raw_response_wrapper(
            repos.list_watchers,
        )
        self.merge_branch = to_raw_response_wrapper(
            repos.merge_branch,
        )
        self.sync_with_upstream = to_raw_response_wrapper(
            repos.sync_with_upstream,
        )
        self.transfer = to_raw_response_wrapper(
            repos.transfer,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._repos.actions)

    @cached_property
    def assignees(self) -> AssigneesResourceWithRawResponse:
        return AssigneesResourceWithRawResponse(self._repos.assignees)

    @cached_property
    def attestations(self) -> AttestationsResourceWithRawResponse:
        return AttestationsResourceWithRawResponse(self._repos.attestations)

    @cached_property
    def autolinks(self) -> AutolinksResourceWithRawResponse:
        return AutolinksResourceWithRawResponse(self._repos.autolinks)

    @cached_property
    def automated_security_fixes(self) -> AutomatedSecurityFixesResourceWithRawResponse:
        return AutomatedSecurityFixesResourceWithRawResponse(self._repos.automated_security_fixes)

    @cached_property
    def branches(self) -> BranchesResourceWithRawResponse:
        return BranchesResourceWithRawResponse(self._repos.branches)

    @cached_property
    def check_runs(self) -> CheckRunsResourceWithRawResponse:
        return CheckRunsResourceWithRawResponse(self._repos.check_runs)

    @cached_property
    def check_suites(self) -> CheckSuitesResourceWithRawResponse:
        return CheckSuitesResourceWithRawResponse(self._repos.check_suites)

    @cached_property
    def code_scanning(self) -> CodeScanningResourceWithRawResponse:
        return CodeScanningResourceWithRawResponse(self._repos.code_scanning)

    @cached_property
    def codeowners(self) -> CodeownersResourceWithRawResponse:
        return CodeownersResourceWithRawResponse(self._repos.codeowners)

    @cached_property
    def codespaces(self) -> CodespacesResourceWithRawResponse:
        return CodespacesResourceWithRawResponse(self._repos.codespaces)

    @cached_property
    def collaborators(self) -> CollaboratorsResourceWithRawResponse:
        return CollaboratorsResourceWithRawResponse(self._repos.collaborators)

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._repos.comments)

    @cached_property
    def commits(self) -> CommitsResourceWithRawResponse:
        return CommitsResourceWithRawResponse(self._repos.commits)

    @cached_property
    def community(self) -> CommunityResourceWithRawResponse:
        return CommunityResourceWithRawResponse(self._repos.community)

    @cached_property
    def contents(self) -> ContentsResourceWithRawResponse:
        return ContentsResourceWithRawResponse(self._repos.contents)

    @cached_property
    def dependabot(self) -> DependabotResourceWithRawResponse:
        return DependabotResourceWithRawResponse(self._repos.dependabot)

    @cached_property
    def dependency_graph(self) -> DependencyGraphResourceWithRawResponse:
        return DependencyGraphResourceWithRawResponse(self._repos.dependency_graph)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self._repos.deployments)

    @cached_property
    def environments(self) -> EnvironmentsResourceWithRawResponse:
        return EnvironmentsResourceWithRawResponse(self._repos.environments)

    @cached_property
    def forks(self) -> ForksResourceWithRawResponse:
        return ForksResourceWithRawResponse(self._repos.forks)

    @cached_property
    def git(self) -> GitResourceWithRawResponse:
        return GitResourceWithRawResponse(self._repos.git)

    @cached_property
    def hooks(self) -> HooksResourceWithRawResponse:
        return HooksResourceWithRawResponse(self._repos.hooks)

    @cached_property
    def import_(self) -> ImportResourceWithRawResponse:
        return ImportResourceWithRawResponse(self._repos.import_)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResourceWithRawResponse:
        return InteractionLimitsResourceWithRawResponse(self._repos.interaction_limits)

    @cached_property
    def invitations(self) -> InvitationsResourceWithRawResponse:
        return InvitationsResourceWithRawResponse(self._repos.invitations)

    @cached_property
    def issues(self) -> IssuesResourceWithRawResponse:
        return IssuesResourceWithRawResponse(self._repos.issues)

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._repos.keys)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        return LabelsResourceWithRawResponse(self._repos.labels)

    @cached_property
    def milestones(self) -> MilestonesResourceWithRawResponse:
        return MilestonesResourceWithRawResponse(self._repos.milestones)

    @cached_property
    def notifications(self) -> NotificationsResourceWithRawResponse:
        return NotificationsResourceWithRawResponse(self._repos.notifications)

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._repos.pages)

    @cached_property
    def private_vulnerability_reporting(self) -> PrivateVulnerabilityReportingResourceWithRawResponse:
        return PrivateVulnerabilityReportingResourceWithRawResponse(self._repos.private_vulnerability_reporting)

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._repos.projects)

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        return PropertiesResourceWithRawResponse(self._repos.properties)

    @cached_property
    def pulls(self) -> PullsResourceWithRawResponse:
        return PullsResourceWithRawResponse(self._repos.pulls)

    @cached_property
    def readme(self) -> ReadmeResourceWithRawResponse:
        return ReadmeResourceWithRawResponse(self._repos.readme)

    @cached_property
    def releases(self) -> ReleasesResourceWithRawResponse:
        return ReleasesResourceWithRawResponse(self._repos.releases)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._repos.rules)

    @cached_property
    def rulesets(self) -> RulesetsResourceWithRawResponse:
        return RulesetsResourceWithRawResponse(self._repos.rulesets)

    @cached_property
    def secret_scanning(self) -> SecretScanningResourceWithRawResponse:
        return SecretScanningResourceWithRawResponse(self._repos.secret_scanning)

    @cached_property
    def security_advisories(self) -> SecurityAdvisoriesResourceWithRawResponse:
        return SecurityAdvisoriesResourceWithRawResponse(self._repos.security_advisories)

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self._repos.stats)

    @cached_property
    def subscription(self) -> SubscriptionResourceWithRawResponse:
        return SubscriptionResourceWithRawResponse(self._repos.subscription)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._repos.tags)

    @cached_property
    def topics(self) -> TopicsResourceWithRawResponse:
        return TopicsResourceWithRawResponse(self._repos.topics)

    @cached_property
    def traffic(self) -> TrafficResourceWithRawResponse:
        return TrafficResourceWithRawResponse(self._repos.traffic)

    @cached_property
    def vulnerability_alerts(self) -> VulnerabilityAlertsResourceWithRawResponse:
        return VulnerabilityAlertsResourceWithRawResponse(self._repos.vulnerability_alerts)


class AsyncReposResourceWithRawResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.retrieve = async_to_raw_response_wrapper(
            repos.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            repos.update,
        )
        self.delete = async_to_raw_response_wrapper(
            repos.delete,
        )
        self.compare_commits = async_to_raw_response_wrapper(
            repos.compare_commits,
        )
        self.create_commit_status = async_to_raw_response_wrapper(
            repos.create_commit_status,
        )
        self.create_dispatch_event = async_to_raw_response_wrapper(
            repos.create_dispatch_event,
        )
        self.create_from_template = async_to_raw_response_wrapper(
            repos.create_from_template,
        )
        self.download_tarball = async_to_raw_response_wrapper(
            repos.download_tarball,
        )
        self.download_zipball = async_to_raw_response_wrapper(
            repos.download_zipball,
        )
        self.get_code_security_configuration = async_to_raw_response_wrapper(
            repos.get_code_security_configuration,
        )
        self.get_installation = async_to_raw_response_wrapper(
            repos.get_installation,
        )
        self.get_license = async_to_raw_response_wrapper(
            repos.get_license,
        )
        self.list_activity = async_to_raw_response_wrapper(
            repos.list_activity,
        )
        self.list_contributors = async_to_raw_response_wrapper(
            repos.list_contributors,
        )
        self.list_events = async_to_raw_response_wrapper(
            repos.list_events,
        )
        self.list_languages = async_to_raw_response_wrapper(
            repos.list_languages,
        )
        self.list_stargazers = async_to_raw_response_wrapper(
            repos.list_stargazers,
        )
        self.list_teams = async_to_raw_response_wrapper(
            repos.list_teams,
        )
        self.list_watchers = async_to_raw_response_wrapper(
            repos.list_watchers,
        )
        self.merge_branch = async_to_raw_response_wrapper(
            repos.merge_branch,
        )
        self.sync_with_upstream = async_to_raw_response_wrapper(
            repos.sync_with_upstream,
        )
        self.transfer = async_to_raw_response_wrapper(
            repos.transfer,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._repos.actions)

    @cached_property
    def assignees(self) -> AsyncAssigneesResourceWithRawResponse:
        return AsyncAssigneesResourceWithRawResponse(self._repos.assignees)

    @cached_property
    def attestations(self) -> AsyncAttestationsResourceWithRawResponse:
        return AsyncAttestationsResourceWithRawResponse(self._repos.attestations)

    @cached_property
    def autolinks(self) -> AsyncAutolinksResourceWithRawResponse:
        return AsyncAutolinksResourceWithRawResponse(self._repos.autolinks)

    @cached_property
    def automated_security_fixes(self) -> AsyncAutomatedSecurityFixesResourceWithRawResponse:
        return AsyncAutomatedSecurityFixesResourceWithRawResponse(self._repos.automated_security_fixes)

    @cached_property
    def branches(self) -> AsyncBranchesResourceWithRawResponse:
        return AsyncBranchesResourceWithRawResponse(self._repos.branches)

    @cached_property
    def check_runs(self) -> AsyncCheckRunsResourceWithRawResponse:
        return AsyncCheckRunsResourceWithRawResponse(self._repos.check_runs)

    @cached_property
    def check_suites(self) -> AsyncCheckSuitesResourceWithRawResponse:
        return AsyncCheckSuitesResourceWithRawResponse(self._repos.check_suites)

    @cached_property
    def code_scanning(self) -> AsyncCodeScanningResourceWithRawResponse:
        return AsyncCodeScanningResourceWithRawResponse(self._repos.code_scanning)

    @cached_property
    def codeowners(self) -> AsyncCodeownersResourceWithRawResponse:
        return AsyncCodeownersResourceWithRawResponse(self._repos.codeowners)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResourceWithRawResponse:
        return AsyncCodespacesResourceWithRawResponse(self._repos.codespaces)

    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResourceWithRawResponse:
        return AsyncCollaboratorsResourceWithRawResponse(self._repos.collaborators)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._repos.comments)

    @cached_property
    def commits(self) -> AsyncCommitsResourceWithRawResponse:
        return AsyncCommitsResourceWithRawResponse(self._repos.commits)

    @cached_property
    def community(self) -> AsyncCommunityResourceWithRawResponse:
        return AsyncCommunityResourceWithRawResponse(self._repos.community)

    @cached_property
    def contents(self) -> AsyncContentsResourceWithRawResponse:
        return AsyncContentsResourceWithRawResponse(self._repos.contents)

    @cached_property
    def dependabot(self) -> AsyncDependabotResourceWithRawResponse:
        return AsyncDependabotResourceWithRawResponse(self._repos.dependabot)

    @cached_property
    def dependency_graph(self) -> AsyncDependencyGraphResourceWithRawResponse:
        return AsyncDependencyGraphResourceWithRawResponse(self._repos.dependency_graph)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self._repos.deployments)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithRawResponse:
        return AsyncEnvironmentsResourceWithRawResponse(self._repos.environments)

    @cached_property
    def forks(self) -> AsyncForksResourceWithRawResponse:
        return AsyncForksResourceWithRawResponse(self._repos.forks)

    @cached_property
    def git(self) -> AsyncGitResourceWithRawResponse:
        return AsyncGitResourceWithRawResponse(self._repos.git)

    @cached_property
    def hooks(self) -> AsyncHooksResourceWithRawResponse:
        return AsyncHooksResourceWithRawResponse(self._repos.hooks)

    @cached_property
    def import_(self) -> AsyncImportResourceWithRawResponse:
        return AsyncImportResourceWithRawResponse(self._repos.import_)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResourceWithRawResponse:
        return AsyncInteractionLimitsResourceWithRawResponse(self._repos.interaction_limits)

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithRawResponse:
        return AsyncInvitationsResourceWithRawResponse(self._repos.invitations)

    @cached_property
    def issues(self) -> AsyncIssuesResourceWithRawResponse:
        return AsyncIssuesResourceWithRawResponse(self._repos.issues)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._repos.keys)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        return AsyncLabelsResourceWithRawResponse(self._repos.labels)

    @cached_property
    def milestones(self) -> AsyncMilestonesResourceWithRawResponse:
        return AsyncMilestonesResourceWithRawResponse(self._repos.milestones)

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithRawResponse:
        return AsyncNotificationsResourceWithRawResponse(self._repos.notifications)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._repos.pages)

    @cached_property
    def private_vulnerability_reporting(self) -> AsyncPrivateVulnerabilityReportingResourceWithRawResponse:
        return AsyncPrivateVulnerabilityReportingResourceWithRawResponse(self._repos.private_vulnerability_reporting)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._repos.projects)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        return AsyncPropertiesResourceWithRawResponse(self._repos.properties)

    @cached_property
    def pulls(self) -> AsyncPullsResourceWithRawResponse:
        return AsyncPullsResourceWithRawResponse(self._repos.pulls)

    @cached_property
    def readme(self) -> AsyncReadmeResourceWithRawResponse:
        return AsyncReadmeResourceWithRawResponse(self._repos.readme)

    @cached_property
    def releases(self) -> AsyncReleasesResourceWithRawResponse:
        return AsyncReleasesResourceWithRawResponse(self._repos.releases)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._repos.rules)

    @cached_property
    def rulesets(self) -> AsyncRulesetsResourceWithRawResponse:
        return AsyncRulesetsResourceWithRawResponse(self._repos.rulesets)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResourceWithRawResponse:
        return AsyncSecretScanningResourceWithRawResponse(self._repos.secret_scanning)

    @cached_property
    def security_advisories(self) -> AsyncSecurityAdvisoriesResourceWithRawResponse:
        return AsyncSecurityAdvisoriesResourceWithRawResponse(self._repos.security_advisories)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self._repos.stats)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithRawResponse:
        return AsyncSubscriptionResourceWithRawResponse(self._repos.subscription)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._repos.tags)

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithRawResponse:
        return AsyncTopicsResourceWithRawResponse(self._repos.topics)

    @cached_property
    def traffic(self) -> AsyncTrafficResourceWithRawResponse:
        return AsyncTrafficResourceWithRawResponse(self._repos.traffic)

    @cached_property
    def vulnerability_alerts(self) -> AsyncVulnerabilityAlertsResourceWithRawResponse:
        return AsyncVulnerabilityAlertsResourceWithRawResponse(self._repos.vulnerability_alerts)


class ReposResourceWithStreamingResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.retrieve = to_streamed_response_wrapper(
            repos.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            repos.update,
        )
        self.delete = to_streamed_response_wrapper(
            repos.delete,
        )
        self.compare_commits = to_streamed_response_wrapper(
            repos.compare_commits,
        )
        self.create_commit_status = to_streamed_response_wrapper(
            repos.create_commit_status,
        )
        self.create_dispatch_event = to_streamed_response_wrapper(
            repos.create_dispatch_event,
        )
        self.create_from_template = to_streamed_response_wrapper(
            repos.create_from_template,
        )
        self.download_tarball = to_streamed_response_wrapper(
            repos.download_tarball,
        )
        self.download_zipball = to_streamed_response_wrapper(
            repos.download_zipball,
        )
        self.get_code_security_configuration = to_streamed_response_wrapper(
            repos.get_code_security_configuration,
        )
        self.get_installation = to_streamed_response_wrapper(
            repos.get_installation,
        )
        self.get_license = to_streamed_response_wrapper(
            repos.get_license,
        )
        self.list_activity = to_streamed_response_wrapper(
            repos.list_activity,
        )
        self.list_contributors = to_streamed_response_wrapper(
            repos.list_contributors,
        )
        self.list_events = to_streamed_response_wrapper(
            repos.list_events,
        )
        self.list_languages = to_streamed_response_wrapper(
            repos.list_languages,
        )
        self.list_stargazers = to_streamed_response_wrapper(
            repos.list_stargazers,
        )
        self.list_teams = to_streamed_response_wrapper(
            repos.list_teams,
        )
        self.list_watchers = to_streamed_response_wrapper(
            repos.list_watchers,
        )
        self.merge_branch = to_streamed_response_wrapper(
            repos.merge_branch,
        )
        self.sync_with_upstream = to_streamed_response_wrapper(
            repos.sync_with_upstream,
        )
        self.transfer = to_streamed_response_wrapper(
            repos.transfer,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._repos.actions)

    @cached_property
    def assignees(self) -> AssigneesResourceWithStreamingResponse:
        return AssigneesResourceWithStreamingResponse(self._repos.assignees)

    @cached_property
    def attestations(self) -> AttestationsResourceWithStreamingResponse:
        return AttestationsResourceWithStreamingResponse(self._repos.attestations)

    @cached_property
    def autolinks(self) -> AutolinksResourceWithStreamingResponse:
        return AutolinksResourceWithStreamingResponse(self._repos.autolinks)

    @cached_property
    def automated_security_fixes(self) -> AutomatedSecurityFixesResourceWithStreamingResponse:
        return AutomatedSecurityFixesResourceWithStreamingResponse(self._repos.automated_security_fixes)

    @cached_property
    def branches(self) -> BranchesResourceWithStreamingResponse:
        return BranchesResourceWithStreamingResponse(self._repos.branches)

    @cached_property
    def check_runs(self) -> CheckRunsResourceWithStreamingResponse:
        return CheckRunsResourceWithStreamingResponse(self._repos.check_runs)

    @cached_property
    def check_suites(self) -> CheckSuitesResourceWithStreamingResponse:
        return CheckSuitesResourceWithStreamingResponse(self._repos.check_suites)

    @cached_property
    def code_scanning(self) -> CodeScanningResourceWithStreamingResponse:
        return CodeScanningResourceWithStreamingResponse(self._repos.code_scanning)

    @cached_property
    def codeowners(self) -> CodeownersResourceWithStreamingResponse:
        return CodeownersResourceWithStreamingResponse(self._repos.codeowners)

    @cached_property
    def codespaces(self) -> CodespacesResourceWithStreamingResponse:
        return CodespacesResourceWithStreamingResponse(self._repos.codespaces)

    @cached_property
    def collaborators(self) -> CollaboratorsResourceWithStreamingResponse:
        return CollaboratorsResourceWithStreamingResponse(self._repos.collaborators)

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._repos.comments)

    @cached_property
    def commits(self) -> CommitsResourceWithStreamingResponse:
        return CommitsResourceWithStreamingResponse(self._repos.commits)

    @cached_property
    def community(self) -> CommunityResourceWithStreamingResponse:
        return CommunityResourceWithStreamingResponse(self._repos.community)

    @cached_property
    def contents(self) -> ContentsResourceWithStreamingResponse:
        return ContentsResourceWithStreamingResponse(self._repos.contents)

    @cached_property
    def dependabot(self) -> DependabotResourceWithStreamingResponse:
        return DependabotResourceWithStreamingResponse(self._repos.dependabot)

    @cached_property
    def dependency_graph(self) -> DependencyGraphResourceWithStreamingResponse:
        return DependencyGraphResourceWithStreamingResponse(self._repos.dependency_graph)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self._repos.deployments)

    @cached_property
    def environments(self) -> EnvironmentsResourceWithStreamingResponse:
        return EnvironmentsResourceWithStreamingResponse(self._repos.environments)

    @cached_property
    def forks(self) -> ForksResourceWithStreamingResponse:
        return ForksResourceWithStreamingResponse(self._repos.forks)

    @cached_property
    def git(self) -> GitResourceWithStreamingResponse:
        return GitResourceWithStreamingResponse(self._repos.git)

    @cached_property
    def hooks(self) -> HooksResourceWithStreamingResponse:
        return HooksResourceWithStreamingResponse(self._repos.hooks)

    @cached_property
    def import_(self) -> ImportResourceWithStreamingResponse:
        return ImportResourceWithStreamingResponse(self._repos.import_)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResourceWithStreamingResponse:
        return InteractionLimitsResourceWithStreamingResponse(self._repos.interaction_limits)

    @cached_property
    def invitations(self) -> InvitationsResourceWithStreamingResponse:
        return InvitationsResourceWithStreamingResponse(self._repos.invitations)

    @cached_property
    def issues(self) -> IssuesResourceWithStreamingResponse:
        return IssuesResourceWithStreamingResponse(self._repos.issues)

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._repos.keys)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        return LabelsResourceWithStreamingResponse(self._repos.labels)

    @cached_property
    def milestones(self) -> MilestonesResourceWithStreamingResponse:
        return MilestonesResourceWithStreamingResponse(self._repos.milestones)

    @cached_property
    def notifications(self) -> NotificationsResourceWithStreamingResponse:
        return NotificationsResourceWithStreamingResponse(self._repos.notifications)

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._repos.pages)

    @cached_property
    def private_vulnerability_reporting(self) -> PrivateVulnerabilityReportingResourceWithStreamingResponse:
        return PrivateVulnerabilityReportingResourceWithStreamingResponse(self._repos.private_vulnerability_reporting)

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._repos.projects)

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        return PropertiesResourceWithStreamingResponse(self._repos.properties)

    @cached_property
    def pulls(self) -> PullsResourceWithStreamingResponse:
        return PullsResourceWithStreamingResponse(self._repos.pulls)

    @cached_property
    def readme(self) -> ReadmeResourceWithStreamingResponse:
        return ReadmeResourceWithStreamingResponse(self._repos.readme)

    @cached_property
    def releases(self) -> ReleasesResourceWithStreamingResponse:
        return ReleasesResourceWithStreamingResponse(self._repos.releases)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._repos.rules)

    @cached_property
    def rulesets(self) -> RulesetsResourceWithStreamingResponse:
        return RulesetsResourceWithStreamingResponse(self._repos.rulesets)

    @cached_property
    def secret_scanning(self) -> SecretScanningResourceWithStreamingResponse:
        return SecretScanningResourceWithStreamingResponse(self._repos.secret_scanning)

    @cached_property
    def security_advisories(self) -> SecurityAdvisoriesResourceWithStreamingResponse:
        return SecurityAdvisoriesResourceWithStreamingResponse(self._repos.security_advisories)

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self._repos.stats)

    @cached_property
    def subscription(self) -> SubscriptionResourceWithStreamingResponse:
        return SubscriptionResourceWithStreamingResponse(self._repos.subscription)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._repos.tags)

    @cached_property
    def topics(self) -> TopicsResourceWithStreamingResponse:
        return TopicsResourceWithStreamingResponse(self._repos.topics)

    @cached_property
    def traffic(self) -> TrafficResourceWithStreamingResponse:
        return TrafficResourceWithStreamingResponse(self._repos.traffic)

    @cached_property
    def vulnerability_alerts(self) -> VulnerabilityAlertsResourceWithStreamingResponse:
        return VulnerabilityAlertsResourceWithStreamingResponse(self._repos.vulnerability_alerts)


class AsyncReposResourceWithStreamingResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.retrieve = async_to_streamed_response_wrapper(
            repos.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            repos.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            repos.delete,
        )
        self.compare_commits = async_to_streamed_response_wrapper(
            repos.compare_commits,
        )
        self.create_commit_status = async_to_streamed_response_wrapper(
            repos.create_commit_status,
        )
        self.create_dispatch_event = async_to_streamed_response_wrapper(
            repos.create_dispatch_event,
        )
        self.create_from_template = async_to_streamed_response_wrapper(
            repos.create_from_template,
        )
        self.download_tarball = async_to_streamed_response_wrapper(
            repos.download_tarball,
        )
        self.download_zipball = async_to_streamed_response_wrapper(
            repos.download_zipball,
        )
        self.get_code_security_configuration = async_to_streamed_response_wrapper(
            repos.get_code_security_configuration,
        )
        self.get_installation = async_to_streamed_response_wrapper(
            repos.get_installation,
        )
        self.get_license = async_to_streamed_response_wrapper(
            repos.get_license,
        )
        self.list_activity = async_to_streamed_response_wrapper(
            repos.list_activity,
        )
        self.list_contributors = async_to_streamed_response_wrapper(
            repos.list_contributors,
        )
        self.list_events = async_to_streamed_response_wrapper(
            repos.list_events,
        )
        self.list_languages = async_to_streamed_response_wrapper(
            repos.list_languages,
        )
        self.list_stargazers = async_to_streamed_response_wrapper(
            repos.list_stargazers,
        )
        self.list_teams = async_to_streamed_response_wrapper(
            repos.list_teams,
        )
        self.list_watchers = async_to_streamed_response_wrapper(
            repos.list_watchers,
        )
        self.merge_branch = async_to_streamed_response_wrapper(
            repos.merge_branch,
        )
        self.sync_with_upstream = async_to_streamed_response_wrapper(
            repos.sync_with_upstream,
        )
        self.transfer = async_to_streamed_response_wrapper(
            repos.transfer,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._repos.actions)

    @cached_property
    def assignees(self) -> AsyncAssigneesResourceWithStreamingResponse:
        return AsyncAssigneesResourceWithStreamingResponse(self._repos.assignees)

    @cached_property
    def attestations(self) -> AsyncAttestationsResourceWithStreamingResponse:
        return AsyncAttestationsResourceWithStreamingResponse(self._repos.attestations)

    @cached_property
    def autolinks(self) -> AsyncAutolinksResourceWithStreamingResponse:
        return AsyncAutolinksResourceWithStreamingResponse(self._repos.autolinks)

    @cached_property
    def automated_security_fixes(self) -> AsyncAutomatedSecurityFixesResourceWithStreamingResponse:
        return AsyncAutomatedSecurityFixesResourceWithStreamingResponse(self._repos.automated_security_fixes)

    @cached_property
    def branches(self) -> AsyncBranchesResourceWithStreamingResponse:
        return AsyncBranchesResourceWithStreamingResponse(self._repos.branches)

    @cached_property
    def check_runs(self) -> AsyncCheckRunsResourceWithStreamingResponse:
        return AsyncCheckRunsResourceWithStreamingResponse(self._repos.check_runs)

    @cached_property
    def check_suites(self) -> AsyncCheckSuitesResourceWithStreamingResponse:
        return AsyncCheckSuitesResourceWithStreamingResponse(self._repos.check_suites)

    @cached_property
    def code_scanning(self) -> AsyncCodeScanningResourceWithStreamingResponse:
        return AsyncCodeScanningResourceWithStreamingResponse(self._repos.code_scanning)

    @cached_property
    def codeowners(self) -> AsyncCodeownersResourceWithStreamingResponse:
        return AsyncCodeownersResourceWithStreamingResponse(self._repos.codeowners)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResourceWithStreamingResponse:
        return AsyncCodespacesResourceWithStreamingResponse(self._repos.codespaces)

    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResourceWithStreamingResponse:
        return AsyncCollaboratorsResourceWithStreamingResponse(self._repos.collaborators)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._repos.comments)

    @cached_property
    def commits(self) -> AsyncCommitsResourceWithStreamingResponse:
        return AsyncCommitsResourceWithStreamingResponse(self._repos.commits)

    @cached_property
    def community(self) -> AsyncCommunityResourceWithStreamingResponse:
        return AsyncCommunityResourceWithStreamingResponse(self._repos.community)

    @cached_property
    def contents(self) -> AsyncContentsResourceWithStreamingResponse:
        return AsyncContentsResourceWithStreamingResponse(self._repos.contents)

    @cached_property
    def dependabot(self) -> AsyncDependabotResourceWithStreamingResponse:
        return AsyncDependabotResourceWithStreamingResponse(self._repos.dependabot)

    @cached_property
    def dependency_graph(self) -> AsyncDependencyGraphResourceWithStreamingResponse:
        return AsyncDependencyGraphResourceWithStreamingResponse(self._repos.dependency_graph)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self._repos.deployments)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        return AsyncEnvironmentsResourceWithStreamingResponse(self._repos.environments)

    @cached_property
    def forks(self) -> AsyncForksResourceWithStreamingResponse:
        return AsyncForksResourceWithStreamingResponse(self._repos.forks)

    @cached_property
    def git(self) -> AsyncGitResourceWithStreamingResponse:
        return AsyncGitResourceWithStreamingResponse(self._repos.git)

    @cached_property
    def hooks(self) -> AsyncHooksResourceWithStreamingResponse:
        return AsyncHooksResourceWithStreamingResponse(self._repos.hooks)

    @cached_property
    def import_(self) -> AsyncImportResourceWithStreamingResponse:
        return AsyncImportResourceWithStreamingResponse(self._repos.import_)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResourceWithStreamingResponse:
        return AsyncInteractionLimitsResourceWithStreamingResponse(self._repos.interaction_limits)

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithStreamingResponse:
        return AsyncInvitationsResourceWithStreamingResponse(self._repos.invitations)

    @cached_property
    def issues(self) -> AsyncIssuesResourceWithStreamingResponse:
        return AsyncIssuesResourceWithStreamingResponse(self._repos.issues)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._repos.keys)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        return AsyncLabelsResourceWithStreamingResponse(self._repos.labels)

    @cached_property
    def milestones(self) -> AsyncMilestonesResourceWithStreamingResponse:
        return AsyncMilestonesResourceWithStreamingResponse(self._repos.milestones)

    @cached_property
    def notifications(self) -> AsyncNotificationsResourceWithStreamingResponse:
        return AsyncNotificationsResourceWithStreamingResponse(self._repos.notifications)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._repos.pages)

    @cached_property
    def private_vulnerability_reporting(self) -> AsyncPrivateVulnerabilityReportingResourceWithStreamingResponse:
        return AsyncPrivateVulnerabilityReportingResourceWithStreamingResponse(self._repos.private_vulnerability_reporting)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._repos.projects)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        return AsyncPropertiesResourceWithStreamingResponse(self._repos.properties)

    @cached_property
    def pulls(self) -> AsyncPullsResourceWithStreamingResponse:
        return AsyncPullsResourceWithStreamingResponse(self._repos.pulls)

    @cached_property
    def readme(self) -> AsyncReadmeResourceWithStreamingResponse:
        return AsyncReadmeResourceWithStreamingResponse(self._repos.readme)

    @cached_property
    def releases(self) -> AsyncReleasesResourceWithStreamingResponse:
        return AsyncReleasesResourceWithStreamingResponse(self._repos.releases)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._repos.rules)

    @cached_property
    def rulesets(self) -> AsyncRulesetsResourceWithStreamingResponse:
        return AsyncRulesetsResourceWithStreamingResponse(self._repos.rulesets)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResourceWithStreamingResponse:
        return AsyncSecretScanningResourceWithStreamingResponse(self._repos.secret_scanning)

    @cached_property
    def security_advisories(self) -> AsyncSecurityAdvisoriesResourceWithStreamingResponse:
        return AsyncSecurityAdvisoriesResourceWithStreamingResponse(self._repos.security_advisories)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self._repos.stats)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        return AsyncSubscriptionResourceWithStreamingResponse(self._repos.subscription)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._repos.tags)

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithStreamingResponse:
        return AsyncTopicsResourceWithStreamingResponse(self._repos.topics)

    @cached_property
    def traffic(self) -> AsyncTrafficResourceWithStreamingResponse:
        return AsyncTrafficResourceWithStreamingResponse(self._repos.traffic)

    @cached_property
    def vulnerability_alerts(self) -> AsyncVulnerabilityAlertsResourceWithStreamingResponse:
        return AsyncVulnerabilityAlertsResourceWithStreamingResponse(self._repos.vulnerability_alerts)
