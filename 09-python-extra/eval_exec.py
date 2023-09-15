# Eval and exec are special functions that translate strings into python code

# eval: is less powerful: it can only evaluate code. Which means it can run functions and simple operations but it cannot create new variables

# exec: is more powerful: it can execute any code. You can create variables, run functions etc.

print(eval("5 + 10"))
print(eval("'test'.upper()"))

exec("a = 10")
exec("if True:print('HEY')")
