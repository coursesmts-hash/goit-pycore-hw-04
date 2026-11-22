from pathlib import Path
from typing import Union


def get_cats_info(path: Union[str, Path]) -> list[dict[str, str]]:
    """Читает файл с информацией о котах и возвращает список словарей."""
    cats_info: list[dict[str, str]] = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                parts = cleaned_line.split(",")
                if len(parts) != 3:
                    continue

                cat_id, name, age = (part.strip() for part in parts)
                if not cat_id or not name or not age:
                    continue

                cats_info.append({
                    "id": cat_id,
                    "name": name,
                    "age": age,
                })

        return cats_info

    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except OSError as error:
        print(f"Ошибка при чтении файла: {error}")
        return []


if __name__ == "__main__":
    cats = get_cats_info("cats_file.txt")
    for cat in cats:
        print(cat)
