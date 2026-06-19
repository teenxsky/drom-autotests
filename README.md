# Автотесты drom.ru (Лабораторная работа №8)

UI-автотесты сайта [drom.ru](https://www.drom.ru/) на **Python + Selenium +
pytest** по паттерну **Page Object**, с явными ожиданиями (Explicit Wait),
смешанными локаторами (CSS + XPath) и генерацией **Allure**-отчёта.

Тестируемый функционал — поиск и фильтрация объявлений о продаже автомобилей.

## Установка

> Для работы с проектом потребуется пакетный менеджер [uv](https://docs.astral.sh/uv/getting-started/installation/) и
> python3.14+

```bash
uv install
```

Браузер Chrome должен быть установлен. ChromeDriver скачивается автоматически
через `webdriver-manager`.

## Запуск тестов

```bash
uv run pytest tests/
```

## Allure-отчёт

> Перед открытием allure-отчёта необходим CLI, который можно установить способами,
> перечисленными в [документации](https://allurereport.org/docs/v2/install/)

```bash
# 1) прогнать тесты (результаты лягут в allure-results/)
# 2) сгенерировать и открыть отчёт (нужен установленный Allure CLI)
allure serve allure-results
```
