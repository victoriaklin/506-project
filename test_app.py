import pytest
from app import app

def test_index_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        # Check that the expected text is present on the page
        assert b"Select a Bus Route" in response.data
