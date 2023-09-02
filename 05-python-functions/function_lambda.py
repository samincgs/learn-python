# single line functions Lambdas
# two reasons to use lambdas
# some functions want other functions as arguments
# sort ([1,5,2,3,4], func)

# GUIS graphical user interfaces

x = lambda x: x + 1
simple_calc = lambda a, b: a + b

print(simple_calc(5, 2))

# exercise
# create a lambda function that accepts 1 integer argument
# if the integer is > 5 return hello
# otherwise bye


greet = lambda num: "hello" if num > 5 else "bye"

print(greet(10))
