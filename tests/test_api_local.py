import pytest
import json
from projetcredit import app


def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Bonjour, bienvenue dans mon API"

@pytest.mark.get_request
def test_get_all_id():
    response = app.test_client().get('/id_sk')

    res = json.loads(response.data.decode('utf-8')).get("data")
    assert res['0'] == 100001
    assert res['1'] == 100005
    assert res['2'] == 100013

data = [
    ("100001",95.8768020156236),
    ("100005",89.28363786257623),
    ("100013",98.41193807646683),
    ("100028",92.67129408971392)
]

@pytest.mark.parametrize("SK_ID_CURR,score",data)
def test_get_score(SK_ID_CURR,score):
    response = app.test_client().get(f'/score/?SK_ID_CURR={SK_ID_CURR}')
    res = json.loads(response.data.decode('utf-8')).get("score")
    res_id = json.loads(response.data.decode('utf-8')).get("SK_ID_CURR")
    assert res == score
    assert res_id == SK_ID_CURR