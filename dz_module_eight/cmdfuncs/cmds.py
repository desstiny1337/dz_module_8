import re
from datetime import timedelta, date, datetime
'''
CLASSES
'''

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            self.value = datetime.strptime(value, "%m/%d/%Y").date()
        except ValueError:
            raise ValueError("Invalid date format.Use mm/dd/yyyy")

class Name(Field):
    def __init__(self, name):
        super().__init__(name)





class Phone(Field):
    def __init__(self, phone):
        if not relevant_phone(phone):
            raise ValueError('It must contain 10 digits')
        super().__init__(phone)
    def relevant_phone(phone):
        return isinstance(phone, str) and re.match(r'^\d{10}$', phone)
