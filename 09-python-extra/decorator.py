# Decorators are functions that decorate other functions, we essentially wrap a function around another function
# used to give functions extra functionality without changing it
# For example, we can create a decorator for a function that makes the function execute twice when called

# Applications
# 1. You want to test your code without changing it

# 2. Working on a team and want to avoid unnecessary code changes

# 3. decorators in classes allow you to run code when an attribute is accessed or changed

# Functions recap
# def func():
#     print("Function")

# def wrapper(func):
#     print("hello")
#     func()
#     print("goodbye")

# def function_generator():
#     def new_function():
#         print("New Functions")
#     return new_function

# # wrapper(func)

# functon_gen = function_generator()
# functon_gen()

import time


# Decorators
def decorator(func):
    def wrapper():
        print("decoration begins")
        func()
        print("decoration ends")

    return wrapper


def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f"Duration: {duration}")

    return wrapper


def double_decorator(func):
    def wrapper():
        func()
        func()

    return wrapper


@double_decorator
@decorator
@duration_decorator
def func():
    print("Function")
    time.sleep(1)


func()
# func()
# # func = decorator(func)
# func()
