# Сокращатель ссылок

Сервис сокращения ссылок, реализованный на чистом Python (без сторонних библиотек)

---

## Запуск

```bash
python main.py
```

---

## Структура

Все данные хранятся в словаре `storage`:

```
{ "a1b2": "https://samokat.ru/promo", ... }
```

---

## Функции

| Функция | Описание |
|---|---|
| `add_link(long_url)` | Добавляет ссылку, возвращает короткий код |
| `get_long_url(code)` | Возвращает длинную ссылку по коду |
| `code_exists(code)` | Проверяет, существует ли такой код |
| `find_code_by_url(long_url)` | Обратный поиск: код по длинной ссылке |
| `show_all()` | Выводит все сохранённые пары |
| `generate_code(length)` | Генерирует случайный код (вспомогательная) |

---

## Пример вывода

```
=== Сервис сокращения ссылок ===

Добавлено: a1b2 -> https://stankinapp.ru/schedule/group/2ИТ-421
Добавлено: xZ9k -> https://www.youtube.com/watch?v=dQw4w9WgXcQ
Добавлено: mP3q -> https://www.cornhub.com/
Добавлено: vB8m -> https://samokat.ru/promo
Ссылка уже существует: a1b2 -> https://stankinapp.ru/schedule/group/2ИТ-421

Все сокращённые ссылки:
----------------------------------------
  a1b2 -> https://stankinapp.ru/schedule/group/2ИТ-421
  xZ9k -> https://www.youtube.com/watch?v=dQw4w9WgXcQ
  mP3q -> https://www.cornhub.com/
  vB8m -> https://samokat.ru/promo
----------------------------------------

Получение ссылки по коду 'a1b2':
  Результат: https://stankinapp.ru/schedule/group/2ИТ-421

Проверка существования кода 'xZ9k': True
Проверка существования кода 'xxxx': False

Обратный поиск по 'https://samokat.ru/promo':
  Найден код: vB8m
```