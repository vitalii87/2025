import pytest

# 🔁 Створюється для кожного тесту окремо
@pytest.fixture(scope="function")
def func_data():
    print("🔁 [function scope] створення")
    return ["функціональні дані"]

# 📦 Створюється один раз на весь файл
@pytest.fixture(scope="module")
def module_data():
    print("📦 [module scope] створення")
    return {"модуль": True}

# 🌍 Створюється один раз для всієї сесії тестів
@pytest.fixture(scope="session")
def session_data():
    print("🌍 [session scope] створення")
    return {"сесія": "активна"}

# --- Тести з function scope ---
def test_func_1(func_data):
    print("✅ test_func_1")
    assert "функціональні дані" in func_data

def test_func_2(func_data):
    print("✅ test_func_2")
    assert len(func_data) == 1

# --- Тести з module scope ---
def test_mod_1(module_data):
    print("✅ test_mod_1")
    assert module_data["модуль"]

def test_mod_2(module_data):
    print("✅ test_mod_2")
    assert isinstance(module_data, dict)

# --- Тести з session scope ---
def test_sess_1(session_data):
    print("✅ test_sess_1")
    assert session_data["сесія"] == "активна"

def test_sess_2(session_data):
    print("✅ test_sess_2")
    assert "сесія" in session_data
