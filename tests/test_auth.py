import jwt, pytest, responses

from gitviper.client import GithubClient
from gitviper.exceptions import AuthenticationException
from responses import matchers

from tests.helpers import BASE_URL, DEFAULT_RATE_HEADERS, github_client


app_private_key = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""

app_public_key = """-----BEGIN PUBLIC KEY-----
MIICITANBgkqhkiG9w0BAQEFAAOCAg4AMIICCQKCAgBZizlDa7UfbRkwU7WAR3jD
WfYxd5hbeHVvNFC7RL4qHygxRhFNAd6Pf7GURuo13qGRlL4BHqo54tL4cKX8c5Wq
qUJyXlcjP2mbBAeCE4a1XLwh7kPU9k/7ScaKW8LPiRyvKnx9usRW467r4H7/qRzZ
wElO4JMwIkhWHqIrMCX7rbVLP0PZngPp7Mgc3gXFtf5q3JX86e+n0Mo7FgPqQh9k
nwO8esJiA/2yE17oAOnTx+/+6eOlCw5NDhIidcf/sbN6/HuhmAQiR9WWnUaOrYUH
rUQ4X29kXAyiclN9R8UjZnjSabamnue/qDLNZcVeP+32HbrO17NNcLMVtSaJvcZj
PaJXUuOugkju1ra0UIJYZRpcKF3agP0aO6FWpvVe3AyOR/F+Q0V9J/T3OSwvBdxS
UfdKjhlitBVujo8TQF9aZ//IwcO31x98tmLwQfPGExwwnUZgOENVm4ZTcp3BdOpx
ewymBoROhuXBSLpX5HmkzCniyPoYGyEQZHPeIqFDzer0T5s3a4YpS+gNtb6+5qLU
BujErA99mgw6srvsm9dRT7Ibjih9lCGvccxB9BwDuTqj4QPRxGujTTALv3rel5ff
R8DP0E1bEfkhvZVcJT/iNMfRk+9qjTa9pKEZQiTK0t3MW0muY/IwhBa5U/b8GMPj
O3VSel9CyBDl6wgJ1dQrGwIDAQAB
-----END PUBLIC KEY-----"""

access_token_response = """{
  "token": "ghs_16C7e42F292c6912E7710c838347Ae178B4a",
  "expires_at": "2016-07-11T22:14:10Z",
  "permissions": {
    "issues": "write",
    "contents": "read"
  },
  "repository_selection": "selected",
  "repositories": [
    {
      "id": 1296269,
      "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
      "name": "Hello-World",
      "full_name": "octocat/Hello-World",
      "owner": {
        "login": "octocat",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octocat",
        "html_url": "https://github.com/octocat",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octocat/received_events",
        "type": "User",
        "site_admin": false
      },
      "private": false,
      "html_url": "https://github.com/octocat/Hello-World",
      "description": "This your first repo!",
      "fork": false,
      "url": "https://api.github.com/repos/octocat/Hello-World",
      "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
      "git_url": "git:github.com/octocat/Hello-World.git",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
      "clone_url": "https://github.com/octocat/Hello-World.git",
      "mirror_url": "git:git.example.com/octocat/Hello-World",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
      "svn_url": "https://svn.github.com/octocat/Hello-World",
      "homepage": "https://github.com",
      "language": null,
      "forks_count": 9,
      "stargazers_count": 80,
      "watchers_count": 80,
      "size": 108,
      "default_branch": "master",
      "open_issues_count": 0,
      "is_template": true,
      "topics": [
        "octocat",
        "atom",
        "electron",
        "api"
      ],
      "has_issues": true,
      "has_projects": true,
      "has_wiki": true,
      "has_pages": false,
      "has_downloads": true,
      "archived": false,
      "disabled": false,
      "visibility": "public",
      "pushed_at": "2011-01-26T19:06:43Z",
      "created_at": "2011-01-26T19:01:12Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "permissions": {
        "admin": false,
        "push": false,
        "pull": true
      },
      "allow_rebase_merge": true,
      "template_repository": null,
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "allow_squash_merge": true,
      "allow_auto_merge": false,
      "delete_branch_on_merge": true,
      "allow_merge_commit": true,
      "subscribers_count": 42,
      "network_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "html_url": "https://github.com/licenses/mit"
      },
      "forks": 1,
      "open_issues": 1,
      "watchers": 1
    }
  ]
}"""


@responses.activate
def test_pat_auth():
    gh = github_client()
    assert gh.rate.remaining == 42


@responses.activate
def test_jwt():
    gh = github_client()
    gh.app_id = 42
    gh.app_pk = app_private_key
    gh.installation_id = 99

    encoded_jwt = gh.generate_jwt()
    decoded_jwt = jwt.decode(
        encoded_jwt,
        app_public_key.replace("\\n", "\n"),
        algorithms=[gh.app_pk_algorithm],
    )

    assert decoded_jwt.get("iss") == 42


@responses.activate
def test_app_auth():
    token_resp = responses.post(f"{BASE_URL}/app/installations/99/access_tokens", body=access_token_response)
    responses.get(
        f"{BASE_URL}/rate_limit",
        match=[
            matchers.header_matcher(
                {
                    "Authorization": "Bearer ghs_16C7e42F292c6912E7710c838347Ae178B4a",
                    "Accept": "application/vnd.github+json",
                }
            )
        ],
        headers=DEFAULT_RATE_HEADERS,
    )

    gh = GithubClient(app_id=42, app_pk=app_private_key, installation_id=99)
    assert gh.rate.remaining == 42

    gh._check_token_expiry()
    assert token_resp.call_count == 2


def test_missing_info():
    with pytest.raises(AuthenticationException):
        GithubClient(app_id=123)


@responses.activate
def test_token_error():
    responses.post(f"{BASE_URL}/app/installations/99/access_tokens", status=400)

    with pytest.raises(AuthenticationException):
        GithubClient(app_id=42, app_pk=app_private_key, installation_id=99)
