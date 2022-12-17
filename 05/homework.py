text = input('Please write something: ')
for char in text:
    if char.isdigit():
        if int(char) % 2 == 0:
            print(f'Number {char} is even')
        else:
            print(f'Number {char} is odd')
    elif char.isalpha():
        if char.isupper():
            print(f'Letter {char} is upper case')
        else:
            print(f'Letter {char} is lower case')
    else:
        print(f'{char} is a symbol')

import time
while True:
    print('I love Python')
    time.sleep(4.2)
