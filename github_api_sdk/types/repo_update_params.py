

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RepoUpdateParams",
    "SecurityAndAnalysis",
    "SecurityAndAnalysisAdvancedSecurity",
    "SecurityAndAnalysisCodeSecurity",
    "SecurityAndAnalysisSecretScanning",
    "SecurityAndAnalysisSecretScanningAIDetection",
    "SecurityAndAnalysisSecretScanningNonProviderPatterns",
    "SecurityAndAnalysisSecretScanningPushProtection",
]


class RepoUpdateParams(TypedDict, total=False):
    owner: Required[str]

    allow_auto_merge: bool
    """
    Either `true` to allow auto-merge on pull requests, or `false` to disallow
    auto-merge.
    """

    allow_forking: bool
    """Either `true` to allow private forks, or `false` to prevent private forks."""

    allow_merge_commit: bool
    """
    Either `true` to allow merging pull requests with a merge commit, or `false` to
    prevent merging pull requests with merge commits.
    """

    allow_rebase_merge: bool
    """
    Either `true` to allow rebase-merging pull requests, or `false` to prevent
    rebase-merging.
    """

    allow_squash_merge: bool
    """
    Either `true` to allow squash-merging pull requests, or `false` to prevent
    squash-merging.
    """

    allow_update_branch: bool
    """
    Either `true` to always allow a pull request head branch that is behind its base
    branch to be updated even if it is not required to be up to date before merging,
    or false otherwise.
    """

    archived: bool
    """Whether to archive this repository.

    `false` will unarchive a previously archived repository.
    """

    default_branch: str
    """Updates the default branch for this repository."""

    delete_branch_on_merge: bool
    """
    Either `true` to allow automatically deleting head branches when pull requests
    are merged, or `false` to prevent automatic deletion.
    """

    description: str
    """A short description of the repository."""

    has_issues: bool
    """Either `true` to enable issues for this repository or `false` to disable them."""

    has_projects: bool
    """Either `true` to enable projects for this repository or `false` to disable them.

    **Note:** If you're creating a repository in an organization that has disabled
    repository projects, the default is `false`, and if you pass `true`, the API
    returns an error.
    """

    has_wiki: bool
    """Either `true` to enable the wiki for this repository or `false` to disable it."""

    homepage: str
    """A URL with more information about the repository."""

    is_template: bool
    """
    Either `true` to make this repo available as a template repository or `false` to
    prevent it.
    """

    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"]
    """The default value for a merge commit message.

    - `PR_TITLE` - default to the pull request's title.
    - `PR_BODY` - default to the pull request's body.
    - `BLANK` - default to a blank commit message.
    """

    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"]
    """Required when using `merge_commit_message`.

    The default value for a merge commit title.

    - `PR_TITLE` - default to the pull request's title.
    - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g.,
      Merge pull request #123 from branch-name).
    """

    name: str
    """The name of the repository."""

    private: bool
    """Either `true` to make the repository private or `false` to make it public.

    Default: `false`.  
    **Note**: You will get a `422` error if the organization restricts
    [changing repository visibility](https://docs.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories)
    to organization owners and a non-owner tries to change the value of private.
    """

    security_and_analysis: SecurityAndAnalysis | None
    """
    Specify which security and analysis features to enable or disable for the
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
    """

    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    """The default value for a squash merge commit message:

    - `PR_BODY` - default to the pull request's body.
    - `COMMIT_MESSAGES` - default to the branch's commit messages.
    - `BLANK` - default to a blank commit message.
    """

    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]
    """Required when using `squash_merge_commit_message`.

    The default value for a squash merge commit title:

    - `PR_TITLE` - default to the pull request's title.
    - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or
      the pull request's title (when more than one commit).
    """

    use_squash_pr_title_as_default: bool
    """
    Either `true` to allow squash-merge commits to use pull request title, or
    `false` to use commit message. \\**\\**This property is closing down. Please use
    `squash_merge_commit_title` instead.
    """

    visibility: Literal["public", "private"]
    """The visibility of the repository."""

    web_commit_signoff_required: bool
    """
    Either `true` to require contributors to sign off on web-based commits, or
    `false` to not require contributors to sign off on web-based commits.
    """


class SecurityAndAnalysisAdvancedSecurity(TypedDict, total=False):
    status: str
    """Can be `enabled` or `disabled`."""


class SecurityAndAnalysisCodeSecurity(TypedDict, total=False):
    status: str
    """Can be `enabled` or `disabled`."""


class SecurityAndAnalysisSecretScanning(TypedDict, total=False):
    status: str
    """Can be `enabled` or `disabled`."""


class SecurityAndAnalysisSecretScanningAIDetection(TypedDict, total=False):
    status: str
    """Can be `enabled` or `disabled`."""


class SecurityAndAnalysisSecretScanningNonProviderPatterns(TypedDict, total=False):
    status: str
    """Can be `enabled` or `disabled`."""


class SecurityAndAnalysisSecretScanningPushProtection(TypedDict, total=False):
    status: str
    """Can be `enabled` or `disabled`."""


class SecurityAndAnalysis(TypedDict, total=False):
    advanced_security: SecurityAndAnalysisAdvancedSecurity
    """
    Use the `status` property to enable or disable GitHub Advanced Security for this
    repository. For more information, see
    "[About GitHub Advanced Security](/github/getting-started-with-github/learning-about-github/about-github-advanced-security)."
    """

    code_security: SecurityAndAnalysisCodeSecurity
    """
    Use the `status` property to enable or disable GitHub Code Security for this
    repository.
    """

    secret_scanning: SecurityAndAnalysisSecretScanning
    """
    Use the `status` property to enable or disable secret scanning for this
    repository. For more information, see
    "[About secret scanning](/code-security/secret-security/about-secret-scanning)."
    """

    secret_scanning_ai_detection: SecurityAndAnalysisSecretScanningAIDetection
    """
    Use the `status` property to enable or disable secret scanning AI detection for
    this repository. For more information, see
    "[Responsible detection of generic secrets with AI](https://docs.github.com/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/generic-secret-detection/responsible-ai-generic-secrets)."
    """

    secret_scanning_non_provider_patterns: SecurityAndAnalysisSecretScanningNonProviderPatterns
    """
    Use the `status` property to enable or disable secret scanning non-provider
    patterns for this repository. For more information, see
    "[Supported secret scanning patterns](/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)."
    """

    secret_scanning_push_protection: SecurityAndAnalysisSecretScanningPushProtection
    """
    Use the `status` property to enable or disable secret scanning push protection
    for this repository. For more information, see
    "[Protecting pushes with secret scanning](/code-security/secret-scanning/protecting-pushes-with-secret-scanning)."
    """
