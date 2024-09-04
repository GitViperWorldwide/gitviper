import responses

from gitviper.client import GithubClient
from responses import matchers


DEFAULT_RATE_HEADERS = {
    "x-ratelimit-remaining": "42",
    "x-ratelimit-reset": "9999",
}


@responses.activate
def test_pat_auth():
    base_url = "https://api.github.com"

    responses.get(
        f"{base_url}/rate_limit",
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

    c1 = GithubClient(pat="ghp_abc123")
    assert c1.rate.remaining == 42
