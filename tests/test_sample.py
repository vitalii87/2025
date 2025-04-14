import pytest
import requests

def test_example():
    response = requests.get("https://www.google.com")
    assert response.status_code == 200
