'''
errors processing + datetime manipulations
'''

from datetime import datetime, date, timedelta

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError:
            return 'Not enough arguments given'

    return inner

def change_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Enter an argument'
    return inner

def phone_appear_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return 'Not enough arguments given'
    return inner

def parse_input(user_input):
    if not user_input.strip():
        return None, []
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args

def string_to_date(date_string):
    return datetime.strptime(date_string, '%m/%d/%Y').date()

def date_to_string(date):
    return date.strftime('%m/%d/%Y')

def info_list(user_info):
    info_list = []
    for user in info_list:
        info_list.append({'name': user['name'], 'birthday': string_to_date(user['birthday'])})
    return info_list


def find_next_weekday(start_date, weekday):
    days_last = weekday - start_date.weekday()
    if days_last <= 0:
        days_last += 7
    return start_date + timedelta(days_last)