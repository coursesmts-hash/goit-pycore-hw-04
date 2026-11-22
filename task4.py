def parse_input(user_input: str) -> tuple[str, ...]:
    parts = user_input.strip().split()
    if not parts:
        return ("",)
    cmd, *args = parts
    return cmd.lower(), *args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command. Format: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command. Format: change <name> <new_phone>"
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        return "Invalid command. Format: phone <name>"
    name = args[0]
    if name not in contacts:
        return f"Contact '{name}' not found."
    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
