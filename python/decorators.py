# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# def our_decorator(func):
#     def function_wrapper(x):
#         print('Before calling '+func.__name__)
#         func(x)
#         print('After calling '+func.__name__)
#     return function_wrapper

# def foo(x):
#     print('Foo called with '+str(x))

# print('Call foo before decoration')
# foo('Hi')

# print('Decorate foo with f')
# foo = our_decorator(foo)

# print('Call foo after decoration')
# foo(42)

# from math import sin, cos

# def our_decorator(func):
#     def function_wrapper(x):
#         print("Before calling " + func.__name__)
#         res = func(x)
#         print(res)
#         print("After calling " + func.__name__)
#     return function_wrapper

# @our_decorator
# def succ(n):
#     return n + 1

# sin = our_decorator(sin)
# cos = our_decorator(cos)

# for f in [sin, cos]:
#     f(3.1415)

# succ(10)

# from random import random, randint, choice

# def our_decorator(func):
#     def function_wrapper(*args, **kwargs):
#         print("Before calling " + func.__name__)
#         res = func(*args, **kwargs)
#         print(res)
#         print("After calling " + func.__name__)
#     return function_wrapper

# random = our_decorator(random)
# randint = our_decorator(randint)
# choice = our_decorator(choice)

# random()
# randint(3, 8)
# choice([4, 5, 6])

# def argument_test_natural_number(f):
#     def helper(x):
#         if type(x)==int and x>0:
#             return f(x)
#         else:
#             raise Exception('Argument is not an integer')
#     return helper

# @argument_test_natural_number
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# for i in range(1,10):
#     print(i, factorial(i))

# print(factorial(-1))

def call_counter(func):
    def helper(x):
        helper.calls+=1
        return func(x)
    helper.calls=0
    return helper

@call_counter
def succ(x):
    return x+1

print(succ.calls)

for i in range(10):
    succ(i)

print(succ.calls)




