# generated by datamodel-codegen:
#   filename:  repository_create.json
#   timestamp: 2024-09-03T07:01:11+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class Visibility(Enum):
    public = "public"
    private = "private"


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
