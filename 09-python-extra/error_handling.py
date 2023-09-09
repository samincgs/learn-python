# anticipating errors / exceptions
# try:
#     print(a)
#     print(1/0)
# except ZeroDivisionError:
#     print("something else")
# except NameError:
#     print("does not exist")
# else:
#     print("the else statement")
# finally:
#     print("finally")

# # raising exceptions
# must_be_string = "test string"

# if isinstance(must_be_string, str):
#     print(must_be_string)
# else:
#     raise TypeError("Must be a string")

# # assert
# a = 6
# assert a == 5

list = [1,2,3,4]

try:
    list[99]
except IndexError:
    print("That index does not exist")
else:
    print("That index exists!")
finally:
    print("finished")