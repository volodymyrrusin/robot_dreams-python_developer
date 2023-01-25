from datetime import datetime
import json


# TASK 2: Create decorator with saving text into a txt file
def my_decorator(func):
    def inner(*args, **kwargs):
        text = f'Function name is {func.__name__}, time of execution is {datetime.now()}\n'
        with open('my_deco.txt', 'a') as file:
            file.write(text)
        result = func(*args, **kwargs)
        return result
    return inner


# TASK 3: Create custom exception with saving text into a txt file
class MyCustomException(Exception):
    def __init__(self, message='Custom exception is occurred'):
        text = f'{message}, date of occurrence is {datetime.now()}\n'
        with open('my_exception.txt', 'a') as file:
            file.write(text)
        super().__init__(message)


# TASK 1: Create saving phone book into a json file
try:
    with open('phone_book.json') as json_file:
        phone_book = json.load(json_file)
except IOError:
        phone_book = {}
finally:
    while True:
        command = input('Enter a command: ')
        if command == 'stats':
            print(f'Number of records is {len(phone_book.keys())}')
        elif command == 'add':
            name = input('Enter a name: ')
            if name in phone_book.keys():
                print(f'{name} is already in a phone book')
            else:
                phone_number = input('Enter a phone number: ')
                print(f'{name} is added to a phone book')
                phone_book[name] = phone_number
                with open('phone_book.json', 'w') as json_file:
                    json.dump(phone_book, json_file)
        elif command == 'delete':
            name = input('Enter a name: ')
            if name in phone_book.keys():
                print(f'{name} is deleted from a phone book')
                del phone_book[name]
                with open('phone_book.json', 'w') as json_file:
                    json.dump(phone_book, json_file)
            else:
                print('There is no such name in a phone book')
        elif command == 'list':
            print("List of names in a phone book:")
            for key in phone_book.keys():
                print(key)
        elif command == 'show':
            name = input('Enter a name: ')
            if name in phone_book.keys():
                print(f'{name} phone number is {phone_book[name]}')
            else:
                print('There is no such name in a phone book')
        else:
            print('There is no such command: ')
