import json
import re


# TASK 1
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
                if re.fullmatch(r'^(\+380|380|0)\d{9}$', phone_number):
                    print(f'{name} is added to a phone book')
                    phone_book[name] = phone_number
                    with open('phone_book.json', 'w') as json_file:
                        json.dump(phone_book, json_file)
                else:
                    print('Phone number has an incorrect format')
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


# TASK 2
file = input('Enter the name of the file: ')
with open(file) as f:
    text = f.read()
    regex = r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9._%+-]+\.[A-Z]+'
    new_text = re.sub(regex, '*@*', text)
    print(new_text)


# TASK 3
file = input('Enter the name of the file: ')


def func(m):
    s = m.group(0)
    i = '*' * ((m.end() - m.start()) // 2)
    return f'{s[0]}{i}@{i}{s[-1]}'


with open(file) as f:
    text = f.read()
    regex = r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9._%+-]+\.[A-Z]+'
    new_text = re.sub(regex, func, text)
