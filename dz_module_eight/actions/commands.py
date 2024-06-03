'''
code for commands
'''

from datetime import datetime

from actions.errors import (input_error, change_error, phone_appear_error, info_list)
from cmdfuncs.cmds import Phone, Name
from cmdfuncs.records import AddressBook, Record


@input_error
def add_contact(args, book: AddressBook):
    name, phone, = args
    record = book.find(name)
    msg = 'Contact updated.'
    if record is None:
        record = Record(name)
        book.add_record(record)
        msg = 'Contact added.'
    if phone:
        record.add_phone(phone)
    return msg


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return 'Contact does not exist.'
    record.add_birthday(birthday)
    return 'Birthday added.'

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        return 'Contact does not exist'
    return str(record.birthday) if record.birthday else 'Birthday does not exist.'

@input_error
def birthdays(book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return '\n'.join(f'{entry['name']} - {entry['birthdays_date_str']}' for entry in upcoming_birthdays)
    else:
        return 'No upcoming'

@change_error
def change_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record:
        record.phones = [Phone(phone)]
        return 'Changed'
    else:
        return 'Contact does not exist'

@phone_appear_error
def delete_contact(args, book: AddressBook):
    name = args[0]
    book.remove_name(name)
    return f"Contact {name} deleted."

@phone_appear_error
def show_phone_number(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        return f'{name}`s number: {', '.join(str(ph) for ph in record.phones)}'
    else:
        return 'Contact does not exist'

def string_to_date(date_string):
    return datetime.strptime(date_string, "%d.%m.%Y").date()





