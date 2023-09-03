# a function executes a block of code
# a method belongs to an object and executes a block of code


# def add(a, b):
#     return a + b


# class Test:
#     def __init__(self, add_function):
#         self.add_function = add_function


# test = Test(add_function=add)
# print(test.add_function(2, 4))

# create a Monster class with a parameter called func, store this func as parameter
# create another class Attacks: with bite,strike,slash,kick (each method just prints some text)


class Monster:
    def __init__(self, func):
        self.func = func


class Attacks:
    def __init__(self):
        pass

    def bite(self):
        print("BITES")

    def strike(self):
        print("STRIKE")

    def slash(self):
        print("SLASH")

    def kick(self):
        print("KICK")


attacks = Attacks()
monster = Monster(func=attacks.bite)
print(dir(monster))

monster.func()
