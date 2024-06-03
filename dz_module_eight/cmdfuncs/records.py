'''
class record, adressbook
'''

from collections import UserDict
from datetime import date
from actions.errors import find_next_weekday, date_to_string
from cmdfuncs.cmds import Birthday, Name, Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.birthday = None
        self.phones = []

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [ph for ph in self.phones if ph.value != phone]

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if not phone:
            raise ValueError('Phone not found')
        index = self.phones.index(phone)
        self.phones[index] = Phone(new_phone)

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def __str__(self):
        phones = '; '.join(str(ph) for ph in self.phones)
        birthday = str(self.birthday) if self.birthday else 'Not set'
        return f'Name: {self.name.value}, Birthday: {birthday}, Phones: {phones}'

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        else:
            return 'This name is already taken'

    def find(self, name):
        return self.data.get(name)

    def remove_name(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError('Name not found')

    def get_upcoming_birthdays(self, weekdays = 7):
        today = date.today()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year +1)
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year = find_next_weekday(birthday_this_year, 0)
                if 0 <= (birthday_this_year - today).days <= weekdays:
                    birthday_date_str = date_to_string(birthday_this_year)
                    upcoming_birthdays.append({'name': record.name, 'birthday': birthday_date_str})
        return upcoming_birthdays

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())