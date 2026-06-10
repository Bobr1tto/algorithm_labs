import random
import string

storage = {}


def generate_code(length=4):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def add_link(long_url):
    existing_code = find_code_by_url(long_url)
    if existing_code:
        print(f"Ссылка уже существует: {existing_code} -> {long_url}")
        return existing_code

    code = generate_code()
    while code in storage:
        code = generate_code()

    storage[code] = long_url
    print(f"Добавлено: {code} -> {long_url}")
    return code


def get_long_url(code):
    if code in storage:
        return storage[code]
    return None


def code_exists(code):
    return code in storage


def find_code_by_url(long_url):
    for code, url in storage.items():
        if url == long_url:
            return code
    return None


def show_all():
    if not storage:
        print("Хранилище пусто.")
        return

    print("\nВсе сокращённые ссылки:")
    for code, url in storage.items():
        print(f"  {code} -> {url}")


if __name__ == "__main__":

    code1 = add_link("https://stankinapp.ru/schedule/group/2ИТ-421")
    code2 = add_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    code3 = add_link("https://www.cornhub.com/")
    code4 = add_link("https://samokat.ru/promo")

    add_link("https://stankinapp.ru/schedule/group/2ИТ-421")

    show_all()

    print(f"\nПолучение ссылки по коду '{code1}':")
    url = get_long_url(code1)
    print(f"  Результат: {url}")

    print(f"\nПроверка существования кода '{code2}': {code_exists(code2)}")
    print(f"Проверка существования кода 'xxxx': {code_exists('xxxx')}")

    print("\nОбратный поиск по 'https://samokat.ru/promo':")
    found = find_code_by_url("https://samokat.ru/promo")
    print(f"  Найден код: {found}")
