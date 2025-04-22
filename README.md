# 🧪 QA Automation Project with Playwright (Python)

## 📁 Структура проекту

```
project_root/
├── locators/
│   └── home_page_locators.py
├── pages/
│   ├── base_page.py
│   └── home_page.py
├── tests/
│   └── test_home_page.py
├── conftest.py
├── pytest.ini
└── README.md
```

---

## 🧠 Основні підходи

### ✅ Playwright замість Selenium
- Playwright обрано завдяки його сучасному API, швидкості та підтримці багатьох браузерів.
- **Локатори** у Playwright задаються напряму як CSS-селектори:
  ```python
  self.page.locator("div.logo")
  ```
  або при потребі XPath:
  ```python
  self.page.locator("xpath=//div[@class='logo']")
  ```

### 🧼 Чистий код:
- Локатори винесені в окремі файли у папку `locators`
- Логіка сторінок — у `pages`
- Тести — в `tests`
- **BasePage** реалізує спільну навігацію для всіх сторінок (наприклад, кнопки навігації в хедері)

### 🧩 Page Object Pattern
- Кожна сторінка представлена окремим класом
- Всі методи і локатори зібрані в одному місці

### 🔁 Повторне використання коду
- Метод `go_to_homepage()` винесено в `HomePage`, але URL міг би бути спільним і теж винесеним до конфігурації
- Змінюється лише те, що потрібно — завдяки спадкуванню від `BasePage`

---

## 🧪 Типи тестів

Планується поділ тестів на:
- `smoke` — базові перевірки, чи сайт працює загалом
- `regression` — глибше тестування всієї функціональності

### Приклад маркування:
```python
import pytest

@pytest.mark.smoke
@pytest.mark.regression
```

І запуск:
```
pytest -m smoke
pytest -m regression
```

---

## 🚀 Запуск тестів

**Запуск через термінал:**
```
pytest tests/test_home_page.py
```

**Головне:** не запускати через кнопку у PyCharm, бо браузер може відкриватись в headless-режимі.

---

## ⛏ Тудушки:
- [ ] Винести URL у конфіг
- [ ] Створити `conftest.py` для ініціалізації `page`
- [ ] Додати інші сторінки (наприклад, Contact Us, Signup)
- [ ] Додати інтеграцію в CI (наприклад, GitHub Actions)
- [ ] Додати генерацію HTML-звітів

---

## 📚 Корисні команди

```
# Встановлення Playwright
pip install playwright pytest
playwright install

# Запуск тестів
pytest -v
pytest -m smoke

# HTML-звіт
pytest --html=report.html
```

---

## 🔗 Посилання
- [Playwright Python Docs](https://playwright.dev/python/)
- [Pytest Docs](https://docs.pytest.org/en/latest/)

---

## 💡 Автор: Vit
Проект створено для вдосконалення навичок у QA Automation та покращення структури тестів.

