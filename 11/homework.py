# TASK 1: Creating the decorator
from datetime import datetime


def my_decorator(func):
    def inner(*args, **kwargs):
        print(f'Function name is {func.__name__}, time of execution is {datetime.now()}')
        result = func(*args, **kwargs)
        return result
    return inner


# TASK 2: Creating custom exception
class MyCustomException(Exception):
    def __init__(self, message='Custom exception is occurred'):
        self.message = message
        super().__init__(self.message)


# TASK 3: Creating the context manager
class MyContextManager:
    def __enter__(self):
        print('==========')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print(exc_value)
        print('==========')
        return True


try:
    with MyContextManager() as some_func:
        print('Here must be some code')
except:
    pass


# TASK 4: Creating try-except construction
try:
    print('==========')
    print('Here must be some code')
except Exception as e:
    print(e)
finally:
    print('==========')
