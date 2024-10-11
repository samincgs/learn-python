# learning more about closures

''' Wikipedia says: "A closure is a record storing a function together with an environment: a mapping associating each free
    variable of the function with the value or storage location to which the name was bound when the closure was created. A closure,
    unlike a plain function, allows the function to access those captured variables through the closures reference to them. even when the function
    is invoked outside of their scope.
'''

def outer_func(msg):
    message = msg
    
    def inner_func():
        print(message) 
    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

# print(my_func)

hi_func()
hello_func()