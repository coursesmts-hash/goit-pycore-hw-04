from pathlib import Path
from typing import Union


def total_salary(path: Union[str, Path]) -> tuple[int, float]:
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                parts = cleaned_line.split(",")
                if len(parts) != 2:
                    continue

                _, salary_str = parts
                salary = int(salary_str.strip())
                total += salary
                count += 1

        if count == 0:
            return 0, 0.0

        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0.0
    except (OSError, ValueError) as error:
        print(f"Помилка під час обробки файлу: {error}")
        return 0, 0.0


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
