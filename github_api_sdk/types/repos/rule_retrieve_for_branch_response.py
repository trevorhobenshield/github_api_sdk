

from typing import List, Union
from typing_extensions import TypeAlias

from ..orgs.repository_rule_update import RepositoryRuleUpdate
from .repository_rule_ruleset_info import RepositoryRuleRulesetInfo
from ..orgs.repository_rule_creation import RepositoryRuleCreation
from ..orgs.repository_rule_deletion import RepositoryRuleDeletion
from ..orgs.repository_rule_workflows import RepositoryRuleWorkflows
from ..orgs.repository_rule_merge_queue import RepositoryRuleMergeQueue
from ..orgs.repository_rule_pull_request import RepositoryRulePullRequest
from ..orgs.repository_rule_code_scanning import RepositoryRuleCodeScanning
from ..orgs.repository_rule_max_file_size import RepositoryRuleMaxFileSize
from ..orgs.repository_rule_non_fast_forward import RepositoryRuleNonFastForward
from ..orgs.repository_rule_tag_name_pattern import RepositoryRuleTagNamePattern
from ..orgs.repository_rule_branch_name_pattern import RepositoryRuleBranchNamePattern
from ..orgs.repository_rule_required_signatures import RepositoryRuleRequiredSignatures
from ..orgs.repository_rule_max_file_path_length import RepositoryRuleMaxFilePathLength
from ..orgs.repository_rule_required_deployments import RepositoryRuleRequiredDeployments
from ..orgs.repository_rule_file_path_restriction import RepositoryRuleFilePathRestriction
from ..orgs.repository_rule_commit_message_pattern import RepositoryRuleCommitMessagePattern
from ..orgs.repository_rule_required_status_checks import RepositoryRuleRequiredStatusChecks
from ..orgs.repository_rule_committer_email_pattern import RepositoryRuleCommitterEmailPattern
from ..orgs.repository_rule_required_linear_history import RepositoryRuleRequiredLinearHistory
from ..orgs.repository_rule_file_extension_restriction import RepositoryRuleFileExtensionRestriction
from ..orgs.repository_rule_commit_author_email_pattern import RepositoryRuleCommitAuthorEmailPattern

__all__ = [
    "RuleRetrieveForBranchResponse",
    "RuleRetrieveForBranchResponseItemUnionMember0",
    "RuleRetrieveForBranchResponseItemUnionMember1",
    "RuleRetrieveForBranchResponseItemUnionMember2",
    "RuleRetrieveForBranchResponseItemUnionMember3",
    "RuleRetrieveForBranchResponseItemUnionMember4",
    "RuleRetrieveForBranchResponseItemUnionMember5",
    "RuleRetrieveForBranchResponseItemUnionMember6",
    "RuleRetrieveForBranchResponseItemUnionMember7",
    "RuleRetrieveForBranchResponseItemUnionMember8",
    "RuleRetrieveForBranchResponseItemUnionMember9",
    "RuleRetrieveForBranchResponseItemUnionMember10",
    "RuleRetrieveForBranchResponseItemUnionMember11",
    "RuleRetrieveForBranchResponseItemUnionMember12",
    "RuleRetrieveForBranchResponseItemUnionMember13",
    "RuleRetrieveForBranchResponseItemUnionMember14",
    "RuleRetrieveForBranchResponseItemUnionMember15",
    "RuleRetrieveForBranchResponseItemUnionMember16",
    "RuleRetrieveForBranchResponseItemUnionMember17",
    "RuleRetrieveForBranchResponseItemUnionMember18",
    "RuleRetrieveForBranchResponseItemUnionMember19",
    "RuleRetrieveForBranchResponseItemUnionMember20",
]


class RuleRetrieveForBranchResponseItemUnionMember0(RepositoryRuleCreation, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember1(RepositoryRuleUpdate, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember2(RepositoryRuleDeletion, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember3(RepositoryRuleRequiredLinearHistory, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember4(RepositoryRuleMergeQueue, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember5(RepositoryRuleRequiredDeployments, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember6(RepositoryRuleRequiredSignatures, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember7(RepositoryRulePullRequest, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember8(RepositoryRuleRequiredStatusChecks, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember9(RepositoryRuleNonFastForward, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember10(RepositoryRuleCommitMessagePattern, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember11(RepositoryRuleCommitAuthorEmailPattern, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember12(RepositoryRuleCommitterEmailPattern, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember13(RepositoryRuleBranchNamePattern, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember14(RepositoryRuleTagNamePattern, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember15(RepositoryRuleFilePathRestriction, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember16(RepositoryRuleMaxFilePathLength, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember17(RepositoryRuleFileExtensionRestriction, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember18(RepositoryRuleMaxFileSize, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember19(RepositoryRuleWorkflows, RepositoryRuleRulesetInfo):
    pass


class RuleRetrieveForBranchResponseItemUnionMember20(RepositoryRuleCodeScanning, RepositoryRuleRulesetInfo):
    pass


RuleRetrieveForBranchResponse: TypeAlias = List[
    Union[
        RuleRetrieveForBranchResponseItemUnionMember0,
        RuleRetrieveForBranchResponseItemUnionMember1,
        RuleRetrieveForBranchResponseItemUnionMember2,
        RuleRetrieveForBranchResponseItemUnionMember3,
        RuleRetrieveForBranchResponseItemUnionMember4,
        RuleRetrieveForBranchResponseItemUnionMember5,
        RuleRetrieveForBranchResponseItemUnionMember6,
        RuleRetrieveForBranchResponseItemUnionMember7,
        RuleRetrieveForBranchResponseItemUnionMember8,
        RuleRetrieveForBranchResponseItemUnionMember9,
        RuleRetrieveForBranchResponseItemUnionMember10,
        RuleRetrieveForBranchResponseItemUnionMember11,
        RuleRetrieveForBranchResponseItemUnionMember12,
        RuleRetrieveForBranchResponseItemUnionMember13,
        RuleRetrieveForBranchResponseItemUnionMember14,
        RuleRetrieveForBranchResponseItemUnionMember15,
        RuleRetrieveForBranchResponseItemUnionMember16,
        RuleRetrieveForBranchResponseItemUnionMember17,
        RuleRetrieveForBranchResponseItemUnionMember18,
        RuleRetrieveForBranchResponseItemUnionMember19,
        RuleRetrieveForBranchResponseItemUnionMember20,
    ]
]
