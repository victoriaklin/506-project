import pytest
from app import app

def test_index_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'<select name="route_selection">' in response.data
