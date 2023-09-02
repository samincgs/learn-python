# # combining conditions
money_available = 100
hungry = False
bored = True
# # check if money available > 80 and if hungry is true or is bored

# if money_available > 80 and hungry == True or bored == True:
#     print("eat something fancy")

# # nested if statements
# if "a" in ["a", "b"]:
#     print("a is in the list")
#     if "a".isalpha():
#         print("a is in the alphabet")


# exercise
if money_available > 80:
    print("I have enough money")
    if hungry:
        print("I am hungry")
        if bored:
            print("eat something fancy")
