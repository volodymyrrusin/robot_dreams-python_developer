try:
    phone_book = {}
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
        elif command == 'delete':
            name = input('Enter a name: ')
            if name in phone_book.keys():
                print(f'{name} is deleted from a phone book')
                del phone_book[name]
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
except Exception as e:
    print(e)