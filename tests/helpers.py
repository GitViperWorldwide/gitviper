import responses

from gitviper.client import GithubClient
from responses import matchers


DEFAULT_RATE_HEADERS = {
    "x-ratelimit-remaining": "42",
    "x-ratelimit-reset": "9999",
}

BASE_URL = "https://api.github.com"


def github_client() -> GithubClient:
    responses.get(
        f"{BASE_URL}/rate_limit",
        match=[
            matchers.header_matcher(
                {
                    "Authorization": "Bearer ghp_abc123",
                    "Accept": "application/vnd.github+json",
                }
            )
        ],
        headers=DEFAULT_RATE_HEADERS,
    )

    return GithubClient(pat="ghp_abc123")
