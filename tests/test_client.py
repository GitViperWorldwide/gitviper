import json, responses

from pydantic import BaseModel
from responses import matchers

from tests.helpers import BASE_URL, github_client


@responses.activate
def test_pat_auth():
    gh = github_client()
    assert gh.rate.remaining == 42


def test_app_auth():
    # TODO
    pass


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
