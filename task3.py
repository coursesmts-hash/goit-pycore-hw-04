import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_directory_tree(directory: Path, prefix: str = "") -> None:
    """Рекурсивно выводит дерево поддиректорий и файлов с подсветкой."""
    try:
        entries = sorted(
            directory.iterdir(),
            key=lambda item: (item.is_file(), item.name.lower()),
        )
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Нет доступа: {directory.name}]{Style.RESET_ALL}")
        return

    total = len(entries)
    for index, entry in enumerate(entries):
        is_last = index == total - 1
        connector = "└── " if is_last else "├── "
        extension = "    " if is_last else "│   "

        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{entry.name}/{Style.RESET_ALL}")
            print_directory_tree(entry, prefix + extension)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Использование: python3 task3.py <путь_к_директории>{Style.RESET_ALL}")
        return

    target_path = Path(sys.argv[1])

    if not target_path.exists():
        print(f"{Fore.RED}Указанный путь не существует: {target_path}{Style.RESET_ALL}")
        return

    if not target_path.is_dir():
        print(f"{Fore.RED}Указанный путь не является директорией: {target_path}{Style.RESET_ALL}")
        return

    print(f"{Fore.BLUE}{target_path.name or str(target_path)}/{Style.RESET_ALL}")
    print_directory_tree(target_path)


if __name__ == "__main__":
    main()
