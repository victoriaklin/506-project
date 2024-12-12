import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index_page(client):
    """Test that the index page returns a 200 response."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Select a Bus Route" in rv.data
