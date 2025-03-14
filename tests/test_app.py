import os
import pytest
from flask import Flask


@pytest.fixture(scope='module')
def test_client():
    app = Flask(__name__)
    app.add_url_rule('/test/', 'test', lambda: {'code': '200'})
    with app.test_request_context():
        yield app.test_client()


def test_index_route(test_client):
    response = test_client.get('/test/')
    assert response.status_code == 200

def test_bad_route(test_client):
    response = test_client.get('/foo/')
    assert response.status_code == 404
