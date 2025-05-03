

from typing import Union
from typing_extensions import TypeAlias

from .repository_rule_update import RepositoryRuleUpdate
from .repository_rule_creation import RepositoryRuleCreation
from .repository_rule_deletion import RepositoryRuleDeletion
from .repository_rule_workflows import RepositoryRuleWorkflows
from .repository_rule_merge_queue import RepositoryRuleMergeQueue
from .repository_rule_pull_request import RepositoryRulePullRequest
from .repository_rule_code_scanning import RepositoryRuleCodeScanning
from .repository_rule_max_file_size import RepositoryRuleMaxFileSize
from .repository_rule_non_fast_forward import RepositoryRuleNonFastForward
from .repository_rule_tag_name_pattern import RepositoryRuleTagNamePattern
from .repository_rule_branch_name_pattern import RepositoryRuleBranchNamePattern
from .repository_rule_required_signatures import RepositoryRuleRequiredSignatures
from .repository_rule_max_file_path_length import RepositoryRuleMaxFilePathLength
from .repository_rule_required_deployments import RepositoryRuleRequiredDeployments
from .repository_rule_file_path_restriction import RepositoryRuleFilePathRestriction
from .repository_rule_commit_message_pattern import RepositoryRuleCommitMessagePattern
from .repository_rule_required_status_checks import RepositoryRuleRequiredStatusChecks
from .repository_rule_committer_email_pattern import RepositoryRuleCommitterEmailPattern
from .repository_rule_required_linear_history import RepositoryRuleRequiredLinearHistory
from .repository_rule_file_extension_restriction import RepositoryRuleFileExtensionRestriction
from .repository_rule_commit_author_email_pattern import RepositoryRuleCommitAuthorEmailPattern

__all__ = ["RepositoryRule"]

RepositoryRule: TypeAlias = Union[
    RepositoryRuleCreation,
    RepositoryRuleUpdate,
    RepositoryRuleDeletion,
    RepositoryRuleRequiredLinearHistory,
    RepositoryRuleMergeQueue,
    RepositoryRuleRequiredDeployments,
    RepositoryRuleRequiredSignatures,
    RepositoryRulePullRequest,
    RepositoryRuleRequiredStatusChecks,
    RepositoryRuleNonFastForward,
    RepositoryRuleCommitMessagePattern,
    RepositoryRuleCommitAuthorEmailPattern,
    RepositoryRuleCommitterEmailPattern,
    RepositoryRuleBranchNamePattern,
    RepositoryRuleTagNamePattern,
    RepositoryRuleFilePathRestriction,
    RepositoryRuleMaxFilePathLength,
    RepositoryRuleFileExtensionRestriction,
    RepositoryRuleMaxFileSize,
    RepositoryRuleWorkflows,
    RepositoryRuleCodeScanning,
]
