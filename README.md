# UI Автотесты для effective-mobile.ru

Проект выполнен для тестового задания.  
Содержит UI тесты, покрывающие переходы по основным разделам главной страницы.

## 🛠 Технологии
- Python 3.10
- Playwright
- Pytest
- Allure Report
- Docker

## 🚀 Запуск локально

```
pip install -r requirements.txt
playwright install chromium
pytest --alluredir=allure-results
```

## 🐳 Запуск через Docker

```
docker build -t effective-tests .
docker run effective-tests
```

## 📁 Покрытие
- Переходы по меню
- Проверка URL
- PageObject
- Allure steps
