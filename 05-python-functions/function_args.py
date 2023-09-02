# # # parameters and arguments
# # def test_function(arg1, arg2, arg3, arg4="Argument 4"):
# #     print(arg1)
# #     print(arg2)
# #     print(arg3)
# #     print(arg4)


# # test_function(arg1=1, arg3=True, arg2="1", arg4=["1", "Hello", False])

# # # exercise
# # # create a greeter function with 3 args: person, greet, weekday
# # # person and greet should have default arguments ('Person for person and 'Hello for greet)
# # # inside the function use an f-string to print the greet and the person and also print the weekday
# # # when calling the function use at least one positional argument and 1 keyword argument


# # def greeter(weekday, person="Person", greet="Hello"):
# #     print(f"{greet} {person}, I hope you have a great {weekday}")


# # greeter("Sunday", "Jack")


# def print_all(*arguments):
#     # print all args

#     for argument in arguments:
#         print(argument)


# def print_more(**arguments):
#     print(arguments)
#     # keypack unpacking


# def print_even_more(*args, **kwargs):
#     print(args)
#     print(kwargs)


# # print_all(1, 2, 3, 54, 5, [1, 5, 2, 4, 1])
# print_more(arg1=1, arg2=5, arg4=10)

# exercise
# create a calculator function that prints the sum of an unlimited amount of numbers


def unlimited_calculator(*args):
    result = sum(args)
    print(result)


unlimited_calculator(1, 2, 3, 6, 8, 4)
