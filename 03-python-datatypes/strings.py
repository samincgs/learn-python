# strings

test_var = "test 1"
test_var2 = "test 2"
print(test_var, test_var2)


# quotes inside of strings
# option 1: use different quotations to indicate the different strings
test_var3 = 'He said "This is great" '
# option 2: escape characters
test_var4 = 'Hello"HI" ""'
test_var5 = "Line 1: \tsome text\nLine 2: some more text"
print(test_var4)
print(test_var5)

test_var6 = """
xxx
 xx
 xxx"""

print(test_var6)

# how to get values into strings

name = "Bob"
age = 40

print(f"Hello {name}, you are {age} years old")

# create an f-string that says: Hello, my name is X and my hobby is Y
my_name = "Samin"
my_hobby = "walking"
print(f"Hello, my name is {my_name}\nand my hobby is {my_hobby}")
