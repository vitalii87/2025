
import pytest


def test_multi():
    assert 3 * 3 == 9

@pytest.fixture
def fruit_data():
    return ['apple', 'banana', 'cherry']

def test_fruit(fruit_data):
    assert 'banana' in fruit_data

@pytest.mark.parametrize("x, y, result", [(1, 2, 3), (4, 5, 9), (10, 15, 25)])
def test_addition(x, y, result):
    assert x + y == result