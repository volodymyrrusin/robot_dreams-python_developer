message = input('Please write something: ')
if message.isdigit():
    print('This is an integer number')
    if int(message) % 2 == 0:
        print(f'Number {message} is even')
    else:
        print(f'Number {message} is odd')
elif message.isalpha():
    print('This is a word')
    print(f'The length of the {message} is {len(message)} letters')
else:
    print('Input includes some other symbols')