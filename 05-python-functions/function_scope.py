# # functions and scopes
# # a = 10
# # is_true = True


# # def test_func():
# #     capacity = 2
# #     is_true = False
# #     print(capacity)


# # test_func()
# # print(is_true)

# # # pass global variables into functions


# # def add_a(a):
# #     a += 1
# #     return a


# # print(add_a(a))
# # print(a)

# # exercise
# # create 2 global var called multipliera nd has_calculated
# # multiplier should have any integer and has_calculated should be set to the boolean False
# # then create a func called multiply_calculator that takes one argument and calculates the multiplication
# # inside of the function multiply with the global variable multiplier
# # once the calculation is done set has_calculated to True
# # store that new number a variable called result and return it
# # print the return values of the function(after it was called wiyt)

# multiplier = 5
# has_calculated = False


# def multiply_calculator(number):
#     result = multiplier * number
#     global has_calculated
#     has_calculated = True
#     return result


# print(multiply_calculator(2))
# print(has_calculated)
