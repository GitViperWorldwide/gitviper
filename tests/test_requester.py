import json, pytest, responses

from gitviper.exceptions import (
    InvalidRestExpressionException,
    MissingReplacementException,
)
from gitviper.requester import Requester
from requests.sessions import Session
from requests_toolbelt.sessions import BaseUrlSession
from responses import matchers


def test_session_type():
    r1 = Requester(base_url="https://api.github.com")
    assert isinstance(r1.session, BaseUrlSession)

    r2 = Requester(some_keyword="asdf")
    assert isinstance(r2.session, Session)


@responses.activate
def test_rest_parsing():
    base_url = "https://example.com"
    req = Requester(base_url=base_url, stuff="stuff")

    responses.get(
        f"{base_url}/stuff/replaced/stuff",
        match=[matchers.query_param_matcher({"some_query": "value", "anotherquery": "another value"})],
        body="test passed",
    )

    resp1 = req.rest(
        "GET /stuff/{replacement}/{stuff}",
        replacement="replaced",
        some_query="value",
        anotherquery="another value",
    )
    assert resp1.text == "test passed"

    responses.put(
        f"{base_url}/something",
        match=[matchers.json_params_matcher({"a": "json", "body": True})],
        body="great success",
    )
    resp2 = req.rest("PUT something", body=json.dumps({"a": "json", "body": True}))
    assert resp2.text == "great success"

    with pytest.raises(InvalidRestExpressionException):
        req.rest("GIMME /shelter")

    with pytest.raises(MissingReplacementException):
        req.rest("POST /a/missing/{replacement}", rep="stuff")
