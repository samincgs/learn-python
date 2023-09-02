# functions
# def print_line():
#     print("lines!")


# def calculator(num1, num2):
#     result = num1 + num2
#     print(result)


# print_line()
# calculator(2, 3)


# exercise
# if 'plus' do add operation else do 'minus'
def better_calculator(num1, num2, sign):
    if sign == "plus":
        result = num1 + num2
        print(f"The result of the operation is {result}")
    elif sign == "minus":
        result = num1 - num2
        print(f"The result of the operation is {result}")
    else:
        print("The sign does not exist on the calculator")


better_calculator(10, 3, "multiply")
