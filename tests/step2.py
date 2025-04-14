import pytest

# Фікстура створюється один раз для кожної функції (default)
@pytest.fixture(scope="function")
def simple_list():
    print("\n[+] create simple list")
    return [1, 2, 3]

# Фікстура створюється один раз на модуль
@pytest.fixture(scope="module")
def db_connection():
    print("\n[+] connect to fake DB once per module")
    return {"status": "connected"}

def test_list_1(simple_list):
    assert 2 in simple_list

def test_list_2(simple_list):
    assert len(simple_list) == 3

def test_db_1(db_connection):
    assert db_connection["status"] == "connected"

def test_db_2(db_connection):
    assert isinstance(db_connection, dict)
