# generated by datamodel-codegen:
#   filename:  repository.json
#   timestamp: 2024-09-01T02:31:17+00:00

from __future__ import annotations

from enum import Enum
from gitviper.schema.organization import Organization
from pydantic import AnyUrl, AwareDatetime, BaseModel, Field
from typing import Any, Dict, List, Optional


class Permissions(BaseModel):
    admin: bool
    maintain: Optional[bool] = None
    push: bool
    triage: Optional[bool] = None
    pull: bool


class License(BaseModel):
    key: str = Field(..., examples=["mit"])
    name: str = Field(..., examples=["MIT License"])
    url: Optional[AnyUrl] = Field(..., examples=["https://api.github.com/licenses/mit"])
    spdx_id: Optional[str] = Field(..., examples=["MIT"])
    node_id: str = Field(..., examples=["MDc6TGljZW5zZW1pdA=="])
    html_url: Optional[AnyUrl] = None


class SquashMergeCommitTitle(Enum):
    PR_TITLE = "PR_TITLE"
    COMMIT_OR_PR_TITLE = "COMMIT_OR_PR_TITLE"


class SquashMergeCommitMessage(Enum):
    PR_BODY = "PR_BODY"
    COMMIT_MESSAGES = "COMMIT_MESSAGES"
    BLANK = "BLANK"


class MergeCommitTitle(Enum):
    PR_TITLE = "PR_TITLE"
    MERGE_MESSAGE = "MERGE_MESSAGE"


class MergeCommitMessage(Enum):
    PR_BODY = "PR_BODY"
    PR_TITLE = "PR_TITLE"
    BLANK = "BLANK"


class Visibility(Enum):
    public = "public"
    private = "private"
    internal = "internal"


class TemplateRepository(BaseModel):
    id: int = Field(
        ..., description="Unique identifier of the repository", examples=[42]
    )
    node_id: str = Field(..., examples=["MDEwOlJlcG9zaXRvcnkxMjk2MjY5"])
    name: str = Field(
        ..., description="The name of the repository.", examples=["Team Environment"]
    )
    full_name: str = Field(..., examples=["octocat/Hello-World"])
    license: Optional[License] = None
    forks: int
    permissions: Optional[Permissions] = None
    owner: Organization = Field(..., description="A GitHub user.", title="Simple User")
    private: bool = Field(
        ..., description="Whether the repository is private or public."
    )
    html_url: AnyUrl = Field(..., examples=["https://github.com/octocat/Hello-World"])
    description: Optional[str] = Field(..., examples=["This your first repo!"])
    fork: bool
    url: AnyUrl = Field(
        ..., examples=["https://api.github.com/repos/octocat/Hello-World"]
    )
    archive_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}"
        ],
    )
    assignees_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/assignees{/user}"],
    )
    blobs_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}"],
    )
    branches_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/branches{/branch}"],
    )
    collaborators_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}"
        ],
    )
    comments_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/comments{/number}"],
    )
    commits_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/commits{/sha}"]
    )
    compare_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}"
        ],
    )
    contents_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/contents/{+path}"],
    )
    contributors_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/contributors"]
    )
    deployments_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/deployments"]
    )
    downloads_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/downloads"]
    )
    events_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/events"]
    )
    forks_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/forks"]
    )
    git_commits_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}"],
    )
    git_refs_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}"]
    )
    git_tags_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}"]
    )
    git_url: str = Field(..., examples=["git:github.com/octocat/Hello-World.git"])
    issue_comment_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}"
        ],
    )
    issue_events_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}"
        ],
    )
    issues_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/issues{/number}"],
    )
    keys_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/keys{/key_id}"]
    )
    labels_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/labels{/name}"]
    )
    languages_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/languages"]
    )
    merges_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/merges"]
    )
    milestones_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/milestones{/number}"
        ],
    )
    notifications_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}"
        ],
    )
    pulls_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/pulls{/number}"]
    )
    releases_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/releases{/id}"]
    )
    ssh_url: str = Field(..., examples=["git@github.com:octocat/Hello-World.git"])
    stargazers_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/stargazers"]
    )
    statuses_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/statuses/{sha}"]
    )
    subscribers_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/subscribers"]
    )
    subscription_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/subscription"]
    )
    tags_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/tags"]
    )
    teams_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/teams"]
    )
    trees_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}"],
    )
    clone_url: str = Field(..., examples=["https://github.com/octocat/Hello-World.git"])
    mirror_url: Optional[AnyUrl] = Field(
        ..., examples=["git:git.example.com/octocat/Hello-World"]
    )
    hooks_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/hooks"]
    )
    svn_url: AnyUrl = Field(
        ..., examples=["https://svn.github.com/octocat/Hello-World"]
    )
    homepage: Optional[str] = Field(None, examples=["https://github.com"])
    language: Optional[str] = None
    forks_count: int = Field(..., examples=[9])
    stargazers_count: int = Field(..., examples=[80])
    watchers_count: int = Field(..., examples=[80])
    size: int = Field(
        ...,
        description="The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.",
        examples=[108],
    )
    default_branch: str = Field(
        ..., description="The default branch of the repository.", examples=["master"]
    )
    open_issues_count: int = Field(..., examples=[0])
    is_template: Optional[bool] = Field(
        False,
        description="Whether this repository acts as a template that can be used to generate new repositories.",
        examples=[True],
    )
    topics: Optional[List[str]] = None
    has_issues: bool = Field(
        ..., description="Whether issues are enabled.", examples=[True]
    )
    has_projects: bool = Field(
        ..., description="Whether projects are enabled.", examples=[True]
    )
    has_wiki: bool = Field(
        ..., description="Whether the wiki is enabled.", examples=[True]
    )
    has_pages: bool
    has_downloads: bool = Field(
        ..., description="Whether downloads are enabled.", examples=[True]
    )
    has_discussions: Optional[bool] = Field(
        None, description="Whether discussions are enabled.", examples=[True]
    )
    archived: bool = Field(..., description="Whether the repository is archived.")
    disabled: bool = Field(
        ..., description="Returns whether or not this repository disabled."
    )
    visibility: Optional[Visibility] = Field(
        "public", description="The repository visibility: public, private, or internal."
    )
    pushed_at: Optional[AwareDatetime] = Field(..., examples=["2011-01-26T19:06:43Z"])
    created_at: Optional[AwareDatetime] = Field(..., examples=["2011-01-26T19:01:12Z"])
    updated_at: Optional[AwareDatetime] = Field(..., examples=["2011-01-26T19:14:43Z"])
    allow_rebase_merge: Optional[bool] = Field(
        True,
        description="Whether to allow rebase merges for pull requests.",
        examples=[True],
    )
    temp_clone_token: Optional[str] = None
    allow_squash_merge: Optional[bool] = Field(
        True,
        description="Whether to allow squash merges for pull requests.",
        examples=[True],
    )
    allow_auto_merge: Optional[bool] = Field(
        False,
        description="Whether to allow Auto-merge to be used on pull requests.",
        examples=[False],
    )
    delete_branch_on_merge: Optional[bool] = Field(
        False,
        description="Whether to delete head branches when pull requests are merged",
        examples=[False],
    )
    allow_update_branch: Optional[bool] = Field(
        False,
        description="Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging.",
        examples=[False],
    )
    use_squash_pr_title_as_default: Optional[bool] = Field(
        False,
        description="Whether a squash merge commit can use the pull request title as default. **This property has been deprecated. Please use `squash_merge_commit_title` instead.",
    )
    squash_merge_commit_title: Optional[SquashMergeCommitTitle] = Field(
        None,
        description="The default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
    )
    squash_merge_commit_message: Optional[SquashMergeCommitMessage] = Field(
        None,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Optional[MergeCommitTitle] = Field(
        None,
        description="The default value for a merge commit title.\n\n- `PR_TITLE` - default to the pull request's title.\n- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
    )
    merge_commit_message: Optional[MergeCommitMessage] = Field(
        None,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    allow_merge_commit: Optional[bool] = Field(
        True,
        description="Whether to allow merge commits for pull requests.",
        examples=[True],
    )
    allow_forking: Optional[bool] = Field(
        None, description="Whether to allow forking this repo"
    )
    web_commit_signoff_required: Optional[bool] = Field(
        False,
        description="Whether to require contributors to sign off on web-based commits",
    )
    open_issues: int
    watchers: int
    master_branch: Optional[str] = None
    starred_at: Optional[str] = Field(None, examples=['"2020-07-09T00:17:42Z"'])
    anonymous_access_enabled: Optional[bool] = Field(
        None, description="Whether anonymous git access is enabled for this repository"
    )


class CodeOfConduct(BaseModel):
    url: AnyUrl = Field(
        ...,
        examples=["https://api.github.com/repos/github/docs/community/code_of_conduct"],
    )
    key: str = Field(..., examples=["citizen_code_of_conduct"])
    name: str = Field(..., examples=["Citizen Code of Conduct"])
    html_url: Optional[AnyUrl] = Field(
        ..., examples=["https://github.com/github/docs/blob/main/CODE_OF_CONDUCT.md"]
    )


class Status(Enum):
    enabled = "enabled"
    disabled = "disabled"


class AdvancedSecurity(BaseModel):
    status: Optional[Status] = None


class DependabotSecurityUpdates(BaseModel):
    status: Optional[Status] = Field(
        None,
        description="The enablement status of Dependabot security updates for the repository.",
    )


class SecretScanning(BaseModel):
    status: Optional[Status] = None


class SecretScanningPushProtection(BaseModel):
    status: Optional[Status] = None


class SecretScanningNonProviderPatterns(BaseModel):
    status: Optional[Status] = None


class SecurityAndAnalysis(BaseModel):
    advanced_security: Optional[AdvancedSecurity] = None
    dependabot_security_updates: Optional[DependabotSecurityUpdates] = Field(
        None,
        description="Enable or disable Dependabot security updates for the repository.",
    )
    secret_scanning: Optional[SecretScanning] = None
    secret_scanning_push_protection: Optional[SecretScanningPushProtection] = None
    secret_scanning_non_provider_patterns: Optional[
        SecretScanningNonProviderPatterns
    ] = None


class Repository(BaseModel):
    id: int = Field(..., examples=[1296269])
    node_id: str = Field(..., examples=["MDEwOlJlcG9zaXRvcnkxMjk2MjY5"])
    name: str = Field(..., examples=["Hello-World"])
    full_name: str = Field(..., examples=["octocat/Hello-World"])
    owner: Organization = Field(..., description="A GitHub user.", title="Simple User")
    private: bool
    html_url: AnyUrl = Field(..., examples=["https://github.com/octocat/Hello-World"])
    description: Optional[str] = Field(..., examples=["This your first repo!"])
    fork: bool
    url: AnyUrl = Field(
        ..., examples=["https://api.github.com/repos/octocat/Hello-World"]
    )
    archive_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}"
        ],
    )
    assignees_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/assignees{/user}"],
    )
    blobs_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}"],
    )
    branches_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/branches{/branch}"],
    )
    collaborators_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}"
        ],
    )
    comments_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/comments{/number}"],
    )
    commits_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/commits{/sha}"]
    )
    compare_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}"
        ],
    )
    contents_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/contents/{+path}"],
    )
    contributors_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/contributors"]
    )
    deployments_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/deployments"]
    )
    downloads_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/downloads"]
    )
    events_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/events"]
    )
    forks_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/forks"]
    )
    git_commits_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}"],
    )
    git_refs_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}"]
    )
    git_tags_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}"]
    )
    git_url: str = Field(..., examples=["git:github.com/octocat/Hello-World.git"])
    issue_comment_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}"
        ],
    )
    issue_events_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}"
        ],
    )
    issues_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/issues{/number}"],
    )
    keys_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/keys{/key_id}"]
    )
    labels_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/labels{/name}"]
    )
    languages_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/languages"]
    )
    merges_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/merges"]
    )
    milestones_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/milestones{/number}"
        ],
    )
    notifications_url: str = Field(
        ...,
        examples=[
            "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}"
        ],
    )
    pulls_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/pulls{/number}"]
    )
    releases_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/releases{/id}"]
    )
    ssh_url: str = Field(..., examples=["git@github.com:octocat/Hello-World.git"])
    stargazers_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/stargazers"]
    )
    statuses_url: str = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/statuses/{sha}"]
    )
    subscribers_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/subscribers"]
    )
    subscription_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/subscription"]
    )
    tags_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/tags"]
    )
    teams_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/teams"]
    )
    trees_url: str = Field(
        ...,
        examples=["http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}"],
    )
    clone_url: str = Field(..., examples=["https://github.com/octocat/Hello-World.git"])
    mirror_url: Optional[AnyUrl] = Field(
        ..., examples=["git:git.example.com/octocat/Hello-World"]
    )
    hooks_url: AnyUrl = Field(
        ..., examples=["http://api.github.com/repos/octocat/Hello-World/hooks"]
    )
    svn_url: AnyUrl = Field(
        ..., examples=["https://svn.github.com/octocat/Hello-World"]
    )
    homepage: Optional[str] = Field(None, examples=["https://github.com"])
    language: Optional[str] = None
    forks_count: int = Field(..., examples=[9])
    stargazers_count: int = Field(..., examples=[80])
    watchers_count: int = Field(..., examples=[80])
    size: int = Field(
        ...,
        description="The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.",
        examples=[108],
    )
    default_branch: str = Field(..., examples=["master"])
    open_issues_count: int = Field(..., examples=[0])
    is_template: Optional[bool] = Field(None, examples=[True])
    topics: Optional[List[str]] = Field(
        None, examples=["octocat", "atom", "electron", "API"]
    )
    has_issues: bool = Field(..., examples=[True])
    has_projects: bool = Field(..., examples=[True])
    has_wiki: bool = Field(..., examples=[True])
    has_pages: bool
    has_downloads: Optional[bool] = Field(None, examples=[True])
    has_discussions: Optional[bool] = Field(None, examples=[True])
    archived: bool
    disabled: bool = Field(
        ..., description="Returns whether or not this repository disabled."
    )
    visibility: Optional[Visibility] = Field(
        None,
        description="The repository visibility: public, private, or internal.",
        examples=["public"],
    )
    pushed_at: AwareDatetime = Field(..., examples=["2011-01-26T19:06:43Z"])
    created_at: AwareDatetime = Field(..., examples=["2011-01-26T19:01:12Z"])
    updated_at: AwareDatetime = Field(..., examples=["2011-01-26T19:14:43Z"])
    permissions: Optional[Permissions] = None
    allow_rebase_merge: Optional[bool] = Field(None, examples=[True])
    template_repository: Optional[TemplateRepository] = None
    temp_clone_token: Optional[str] = None
    allow_squash_merge: Optional[bool] = Field(None, examples=[True])
    allow_auto_merge: Optional[bool] = Field(None, examples=[False])
    delete_branch_on_merge: Optional[bool] = Field(None, examples=[False])
    allow_merge_commit: Optional[bool] = Field(None, examples=[True])
    allow_update_branch: Optional[bool] = Field(None, examples=[True])
    use_squash_pr_title_as_default: Optional[bool] = Field(None, examples=[False])
    squash_merge_commit_title: Optional[SquashMergeCommitTitle] = Field(
        None,
        description="The default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
        examples=["PR_TITLE"],
    )
    squash_merge_commit_message: Optional[SquashMergeCommitMessage] = Field(
        None,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
        examples=["PR_BODY"],
    )
    merge_commit_title: Optional[MergeCommitTitle] = Field(
        None,
        description="The default value for a merge commit title.\n\n  - `PR_TITLE` - default to the pull request's title.\n  - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
        examples=["PR_TITLE"],
    )
    merge_commit_message: Optional[MergeCommitMessage] = Field(
        None,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
        examples=["PR_BODY"],
    )
    allow_forking: Optional[bool] = Field(None, examples=[True])
    web_commit_signoff_required: Optional[bool] = Field(None, examples=[False])
    subscribers_count: Optional[int] = Field(None, examples=[42])
    network_count: Optional[int] = Field(None, examples=[0])
    license: Optional[License] = None
    organization: Optional[Organization] = None
    parent: Optional[Repository] = Field(
        None, description="A repository on GitHub.", title="Repository"
    )
    source: Optional[Repository] = Field(
        None, description="A repository on GitHub.", title="Repository"
    )
    forks: int
    master_branch: Optional[str] = None
    open_issues: int
    watchers: int
    anonymous_access_enabled: Optional[bool] = Field(
        True, description="Whether anonymous git access is allowed."
    )
    code_of_conduct: Optional[CodeOfConduct] = Field(
        None, description="Code of Conduct Simple", title="Code Of Conduct Simple"
    )
    security_and_analysis: Optional[SecurityAndAnalysis] = None
    custom_properties: Optional[Dict[str, Any]] = Field(
        None,
        description="The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.",
    )


class RepositoryCreate(BaseModel):
    name: str = Field(..., description="The name of the repository.")
    description: Optional[str] = Field(
        None, description="A short description of the repository."
    )
    homepage: Optional[str] = Field(
        None, description="A URL with more information about the repository."
    )
    private: Optional[bool] = Field(
        None, description="Whether the repository is private."
    )
    visibility: Optional[Visibility] = Field(
        None, description="The visibility of the repository."
    )
    has_issues: Optional[bool] = Field(
        None,
        description="Either `true` to enable issues for this repository or `false` to disable them.",
    )
    has_projects: Optional[bool] = Field(
        None,
        description="Either `true` to enable projects for this repository or `false` to disable them. **Note:** If you're creating a repository in an organization that has disabled repository projects, the default is `false`, and if you pass `true`, the API returns an error.",
    )
    has_wiki: Optional[bool] = Field(
        None,
        description="Either `true` to enable the wiki for this repository or `false` to disable it.",
    )
    has_downloads: Optional[bool] = Field(
        None, description="Whether downloads are enabled.", examples=[True]
    )
    is_template: Optional[bool] = Field(
        None,
        description="Either `true` to make this repo available as a template repository or `false` to prevent it.",
    )
    team_id: Optional[int] = Field(
        None,
        description="The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.",
    )
    auto_init: Optional[bool] = Field(
        None, description="Pass `true` to create an initial commit with empty README."
    )
    gitignore_template: Optional[str] = Field(
        None,
        description='Desired language or platform [.gitignore template](https://github.com/github/gitignore) to apply. Use the name of the template without the extension. For example, "Haskell".',
    )
    license_template: Optional[str] = Field(
        None,
        description='Choose an [open source license template](https://choosealicense.com/) that best suits your needs, and then use the [license keyword](https://docs.github.com/articles/licensing-a-repository/#searching-github-by-license-type) as the `license_template` string. For example, "mit" or "mpl-2.0".',
    )
    allow_squash_merge: Optional[bool] = Field(
        None,
        description="Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging.",
    )
    allow_merge_commit: Optional[bool] = Field(
        None,
        description="Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits.",
    )
    allow_rebase_merge: Optional[bool] = Field(
        None,
        description="Either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.",
    )
    allow_auto_merge: Optional[bool] = Field(
        None,
        description="Either `true` to allow auto-merge on pull requests, or `false` to disallow auto-merge.",
    )
    delete_branch_on_merge: Optional[bool] = Field(
        None,
        description="Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion. **The authenticated user must be an organization owner to set this property to `true`.**",
    )
    use_squash_pr_title_as_default: Optional[bool] = Field(
        None,
        description="Either `true` to allow squash-merge commits to use pull request title, or `false` to use commit message. **This property has been deprecated. Please use `squash_merge_commit_title` instead.",
    )
    squash_merge_commit_title: Optional[SquashMergeCommitTitle] = Field(
        None,
        description="Required when using `squash_merge_commit_message`.\n\nThe default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
    )
    squash_merge_commit_message: Optional[SquashMergeCommitMessage] = Field(
        None,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Optional[MergeCommitTitle] = Field(
        None,
        description="Required when using `merge_commit_message`.\n\nThe default value for a merge commit title.\n\n- `PR_TITLE` - default to the pull request's title.\n- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
    )
    merge_commit_message: Optional[MergeCommitMessage] = Field(
        None,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    custom_properties: Optional[Dict[str, Any]] = Field(
        None,
        description="The custom properties for the new repository. The keys are the custom property names, and the values are the corresponding custom property values.",
    )


class RepositoryUpdate(BaseModel):
    name: Optional[str] = Field(None, description="The name of the repository.")
    description: Optional[str] = Field(
        None, description="A short description of the repository."
    )
    homepage: Optional[str] = Field(
        None, description="A URL with more information about the repository."
    )
    private: Optional[bool] = Field(
        None,
        description="Either `true` to make the repository private or `false` to make it public. Default: `false`.  \n**Note**: You will get a `422` error if the organization restricts [changing repository visibility](https://docs.github.com/articles/repository-permission-levels-for-an-organization#changing-the-visibility-of-repositories) to organization owners and a non-owner tries to change the value of private.",
    )
    visibility: Optional[Visibility] = Field(
        None, description="The visibility of the repository."
    )
    security_and_analysis: Optional[SecurityAndAnalysis] = Field(
        None,
        description='Specify which security and analysis features to enable or disable for the repository.\n\nTo use this parameter, you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."\n\nFor example, to enable GitHub Advanced Security, use this data in the body of the `PATCH` request:\n`{ "security_and_analysis": {"advanced_security": { "status": "enabled" } } }`.\n\nYou can check which security and analysis features are currently enabled by using a `GET /repos/{owner}/{repo}` request.',
    )
    has_issues: Optional[bool] = Field(
        None,
        description="Either `true` to enable issues for this repository or `false` to disable them.",
    )
    has_projects: Optional[bool] = Field(
        None,
        description="Either `true` to enable projects for this repository or `false` to disable them. **Note:** If you're creating a repository in an organization that has disabled repository projects, the default is `false`, and if you pass `true`, the API returns an error.",
    )
    has_wiki: Optional[bool] = Field(
        None,
        description="Either `true` to enable the wiki for this repository or `false` to disable it.",
    )
    is_template: Optional[bool] = Field(
        None,
        description="Either `true` to make this repo available as a template repository or `false` to prevent it.",
    )
    default_branch: Optional[str] = Field(
        None, description="Updates the default branch for this repository."
    )
    allow_squash_merge: Optional[bool] = Field(
        None,
        description="Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging.",
    )
    allow_merge_commit: Optional[bool] = Field(
        None,
        description="Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits.",
    )
    allow_rebase_merge: Optional[bool] = Field(
        None,
        description="Either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.",
    )
    allow_auto_merge: Optional[bool] = Field(
        None,
        description="Either `true` to allow auto-merge on pull requests, or `false` to disallow auto-merge.",
    )
    delete_branch_on_merge: Optional[bool] = Field(
        None,
        description="Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion.",
    )
    allow_update_branch: Optional[bool] = Field(
        None,
        description="Either `true` to always allow a pull request head branch that is behind its base branch to be updated even if it is not required to be up to date before merging, or false otherwise.",
    )
    use_squash_pr_title_as_default: Optional[bool] = Field(
        None,
        description="Either `true` to allow squash-merge commits to use pull request title, or `false` to use commit message. **This property has been deprecated. Please use `squash_merge_commit_title` instead.",
    )
    squash_merge_commit_title: Optional[SquashMergeCommitTitle] = Field(
        None,
        description="Required when using `squash_merge_commit_message`.\n\nThe default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
    )
    squash_merge_commit_message: Optional[SquashMergeCommitMessage] = Field(
        None,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Optional[MergeCommitTitle] = Field(
        None,
        description="Required when using `merge_commit_message`.\n\nThe default value for a merge commit title.\n\n- `PR_TITLE` - default to the pull request's title.\n- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
    )
    merge_commit_message: Optional[MergeCommitMessage] = Field(
        None,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    archived: Optional[bool] = Field(
        None,
        description="Whether to archive this repository. `false` will unarchive a previously archived repository.",
    )
    allow_forking: Optional[bool] = Field(
        None,
        description="Either `true` to allow private forks, or `false` to prevent private forks.",
    )
    web_commit_signoff_required: Optional[bool] = Field(
        None,
        description="Either `true` to require contributors to sign off on web-based commits, or `false` to not require contributors to sign off on web-based commits.",
    )
