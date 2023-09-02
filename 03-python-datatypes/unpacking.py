# unpacking can be done on lists and tuples
# only works if you have the same amount of variables as items in lists/tuples
a, b = (10, 5)
print(a, b)

# you can assign multiple variables on a single line
a, b, c = 1, "hello", 4.5
print(a, b, c)


# exercise (switch the values of the two variables)
value_1 = 10
value_2 = "test"

value_1, value_2 = value_2, value_1

print(f"Value 1 is: {value_1}")
print(f"Value 2 is: {value_2}")
