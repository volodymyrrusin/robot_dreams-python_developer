# TASK 1: Program for printing number in Fibonacci sequence using generators

def fib(num):
    a, b = 0, 1
    for _ in range(num + 1):
        yield a
        a, b = b, a + b

def my_func1(n):
    my_gen = fib(n)
    x = 0
    for item in my_gen:
        if x == n:
            print(item)
        x += 1


# TASK 2: Program for printing number in Fibonacci sequence using iterators

class Fib():
    def __init__(self, n):
        self.num = n + 1
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num == 0:
            raise StopIteration
        self.num -= 1
        value = self.a
        b = self.a + self.b
        self.a = self.b
        self.b = b
        return value

def my_func2(n):
    my_iter = Fib(n)
    x = 0
    for item in my_iter:
        if x == n:
            print(item)
        x += 1


# TASK 3: Program for printing number in Fibonacci sequence using recursion

def fib_rec(n, lst):
    a = lst[-2]
    b = lst[-1]
    if len(lst) < n + 1:
        lst = lst + [a + b]
        return fib_rec(n, lst)
    else:
        return lst

def my_func3(n):
    fib_lst = fib_rec(n, [0, 1])
    print(fib_lst[n])


# TASK 4: Program for returning factorial of the number using recursion
def fact_rec(n):
    if n > 0:
        return n * fact_rec(n - 1)
    else:
        return 1
