import sys
from actions.errors import parse_input

from actions.commands import (AddressBook, add_contact, change_contact, delete_contact, show_phone_number, add_birthday,birthdays, show_birthday)
from picklesssss.ppppp import save_data, load_data
def main():
    book = load_data()
    print(f"Welcome to the assistant bot! Here is commands you can use: \n add\n change\n phone\n all\n add-birthday\n show_birthday\n birthdys\n delete\n exit")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            sys.exit(1)

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

            # реалізація

        elif command == "change":
            print(change_contact(args, book))
            # реалізація

        elif command == "phone":
            print( show_phone_number(args, book))
            # реалізація

        elif command == "all":
            print(f'List of contacts: {book}')
            # реалізація

        elif command == "add-birthday":
            print(add_birthday(args, book))
            # реалізація

        elif command == "show-birthday":
            print(show_birthday(args, book))
            # реалізація

        elif command == "birthdays":
            print(birthdays(args, book))
            # реалізація
        elif command == "delete":
            print(delete_contact(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()