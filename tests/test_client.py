import json, jwt, responses

from datetime import datetime, timezone
from gitviper.client import GithubClient, Rate
from pydantic import BaseModel
from requests.adapters import CaseInsensitiveDict
from responses import matchers

from tests.helpers import BASE_URL, DEFAULT_RATE_HEADERS, github_client


def test_rate_parsing():
    now = datetime.now(timezone.utc)
    rate = Rate.from_headers(
        CaseInsensitiveDict(
            **{
                "x-ratelimit-remaining": "not a number",
                "x-ratelimit-reset": "not a number",
            }
        )
    )

    assert rate.remaining == 1
    assert rate.reset.year == now.year
    assert rate.reset.day == now.day


@responses.activate
def test_pagination():
    gh = github_client()

    class TestStuff(BaseModel):
        name: str

    items1 = [TestStuff(name="first"), TestStuff(name="second")]
    items2 = [TestStuff(name="third"), TestStuff(name="fourth")]

    responses.get(
        f"{BASE_URL}/stuff",
        match=[matchers.query_param_matcher({"page": "1", "per_page": "100"})],
        headers={"link": '<https://api.github.com/morestuff?page=2>; rel="next"'},
        body=json.dumps([i.model_dump() for i in items1]),
    )

    responses.get(
        f"{BASE_URL}/morestuff",
        match=[matchers.query_param_matcher({"page": "2", "per_page": "100"})],
        body=json.dumps([i.model_dump() for i in items2]),
    )

    result = gh.paginate("stuff", TestStuff)
    assert result.ok()
    assert len(result.ok()) == 4
    assert result.ok()[0].name == "first"
    assert result.ok()[3].name == "fourth"
